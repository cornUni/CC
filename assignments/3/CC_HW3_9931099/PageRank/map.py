def mapper(graph):
    contributions = []
    for _, node_info in graph.items():
        page_rank = node_info['PageRank']
        adjacency_list = node_info['AdjacencyList']
        num_adjacent_nodes = len(adjacency_list)
        if num_adjacent_nodes > 0:
            contribution = page_rank / num_adjacent_nodes
            for adjacent_node in adjacency_list:
                contributions.append((adjacent_node, contribution))
        else:
            contribution = page_rank / len(graph)
            for n in graph:
                contributions.append((n, contribution))
    return contributions