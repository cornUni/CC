from data import graph
from map import mapper
from reduce import reducer


def main():
        

    num_nodes = len(graph)
    damping_factor = 0.85
    convergence_threshold = 1e-6
    has_converged = False

    # Iteratively apply the MapReduce PageRank computation
    while not has_converged:
        # Map phase
        mapped_contributions = mapper(graph)
        
        # Reduce phase
        new_page_ranks = reducer(mapped_contributions, num_nodes, graph, damping_factor)
        
        # Check for convergence
        has_converged = all(abs(graph[node]['PageRank'] - new_page_ranks[node]) < convergence_threshold for node in graph)
        
        # Update the graph with the new PageRank values
        for node in graph:
            graph[node]['PageRank'] = new_page_ranks[node]

    for node, info in graph.items():
        print(f'PageRank for node {node}   --->   {info["PageRank"]}')

if __name__ == "__main__":
    main()
