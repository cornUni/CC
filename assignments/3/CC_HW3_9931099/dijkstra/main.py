from map import mapper
from reduce import reducer
from graph import GRAPH


def dijkstra(graph, start_node):
    distances = {node: float('inf') if node != start_node else 0 for node in graph}
    to_explore = [start_node]

    attempt_count = 1
    while True:
        print(f'---- Attempt no: {attempt_count} ----\n')
        
        map_output = mapper(graph, to_explore, distances)


        print(f"Mapped values:\n{map_output}\n")
        if not len(map_output):
            break
        reduce_output = reducer(map_output)
        print(f"Reduced values:\n{reduce_output}\n")


        to_explore = []
        for node, potential_dist in reduce_output.items():
             if potential_dist < distances[node]:
                distances[node] = potential_dist
                to_explore.append(node)
                


        attempt_count += 1
    return {node: distance for node, distance in distances.items()}

def main():

    start_node = "A"
    dijkstra_result = dijkstra(GRAPH, start_node)
    print(f'shortest path from node {start_node}\n')
    for node in dijkstra_result:
        print(f'|--> {node} : {dijkstra_result[node]}')

if __name__ == "__main__":
    main()