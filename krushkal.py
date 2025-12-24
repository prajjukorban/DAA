class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False


def kruskal(vertices, edges):
    ds = DisjointSet(vertices)
    mst_cost = 0
    edges.sort(key=lambda x: x[2])

    for u, v, w in edges:
        if ds.union(u, v):
            mst_cost += w

    return mst_cost


vertices = ['A', 'B', 'C', 'D']
edges = [
    ('A', 'B', 2),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('C', 'D', 5)
]

print("Kruskal's MST Cost:", kruskal(vertices, edges))