import heapq

def prim_mst(graph, start):
    visited = set()
    min_heap = [(0, start, None)]  
    mst = []
    total_cost = 0

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_cost += weight
        
        if parent is not None:
            mst.append((parent, node, weight))

        for neighbor, wt in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (wt, neighbor, node))

    return mst, total_cost


graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5)],
    'D': [('B', 4), ('C', 5)]
}

mst, cost = prim_mst(graph, 'A')
print("MST Edges:", mst)
print("Total Cost:", cost)
