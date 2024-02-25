def reducer(contributions, num_nodes, graph,damping_factor=0.85):
    next_page_ranks = {node: (1 - damping_factor) / num_nodes for node in graph}
    for node, contribution in contributions:
        next_page_ranks[node] += damping_factor * contribution
    return next_page_ranks