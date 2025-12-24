from collections import deque

def topological_sort(vertices, edges):
    graph = {v: [] for v in vertices}
    indegree = {v: 0 for v in vertices}

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque([v for v in vertices if indegree[v] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) != len(vertices):
        print("Cycle detected! Topological sort not possible.")
        return None

    return topo_order


vertices = ['A', 'B', 'C', 'D', 'E']
edges = [('A', 'C'), ('B', 'C'), ('C', 'D'), ('D', 'E')]

print("Topological Order:", topological_sort(vertices, edges))