def mapper(graph, to_explore, distances):
    result = []
    for node, node_distance in distances.items():
        if node in to_explore:
            for neighbor, weight in graph[node]["AdjacencyList"].items():
                new_dist = node_distance + weight
                result.append((neighbor, new_dist))
            distances[node] = node_distance
    return result
