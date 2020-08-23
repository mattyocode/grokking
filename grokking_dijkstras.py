#graph data

graph = {
    "start": {
        "a": 5,
        "b": 2,
    },
    "a": {
        "c": 4,
        "d": 2,
    },
    "b": {
        "a": 8,
        "d": 7,
    },
    "c": {
        "d": 6,
        "fin": 3,
    },
    "d": {
        "fin": 1,
    },
    "fin": {
    }
}

#cost data

infinity = float("inf")
costs = {}
costs["a"] = 5
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["fin"] = infinity

#parents data

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def find_lowest_cost_route(costs, graph, parents):
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    return node

find_lowest_cost_route(costs, graph, parents)
print(parents, costs["fin"])