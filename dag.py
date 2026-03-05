from collections import defaultdict

graph = defaultdict(list)

edges = [
    ('A', 'B', 9),
    ('A', 'C', 4),
    ('B', 'C', 10),
    ('B', 'D', 2),
    ('B', 'E', 3),
    ('C', 'D', 2),
    ('C', 'E', 11),
    ('D', 'E', 2)
]

for u, v, w in edges:
    graph[u].append((v, w))

nodes = ['A', 'B', 'C', 'D', 'E']

visited = set()
stack = []

def topological_sort(node):
    visited.add(node)
    for neighbor, _ in graph[node]:
        if neighbor not in visited:
            topological_sort(neighbor)
    stack.append(node)

for node in nodes:
    if node not in visited:
        topological_sort(node)

stack.reverse()

dist = {node: float('inf') for node in nodes}
dist['A'] = 0

for u in stack:
    if dist[u] != float('inf'):
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

print("Shortest distances from A:")
print("---------------------------")
print("Node\tDistance")

for node in nodes:
    print(f"{node}\t{dist[node]}")

with open("dag_shortest_path.txt", "w") as f:
    f.write("Shortest distances from A:\n")
    for node in nodes:
        f.write(f"{node} : {dist[node]}\n")