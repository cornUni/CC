def reducer(mapped_values):
    potential_distances = {}
    for node, distance in mapped_values:
        if node not in potential_distances or distance < potential_distances[node]:
            potential_distances[node] = distance
    return potential_distances