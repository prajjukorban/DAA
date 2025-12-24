def bellman_ford(vertices, edges, source):
    dist = {v: float('inf') for v in vertices}
    dist[source] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            print("Negative weight cycle detected")
            return None

    return dist


vertices = ['A', 'B', 'C', 'D']
edges = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', -3),
    ('B', 'D', 2),
    ('C', 'D', 3)
]

print("Bellman-Ford Shortest Paths:", bellman_ford(vertices, edges, 'A'))