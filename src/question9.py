#question 9 - node path - BFS

def read_graph():
    graph = defaultdict(list)
    print("Enter edges in the format 'A B' to mean A --> B. Type 'done' when finished:")
    while True:
        edge = input("Edge: ").strip()
        if edge.lower() == 'done':
            break
        try:
            u, v = edge.split()
            graph[u].append(v)
        except ValueError:
            print("Invalid format")
    return graph

def find_path(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()
        if current == end:
            return True, path
        if current not in visited:
            visited.add(current)
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return False, []

if __name__ == "__main__":
    graph = read_graph()
    print("\nGraph:", dict(graph))
    start = input("Enter start node: ").strip()
    end = input("Enter end node: ").strip()

    exists, path = find_path(graph, start, end)
    print("\nPath exists?" , exists)
    if exists:
        print("Shortest path:", " --> ".join(path))
    else:
        print("No path exists from", start, "to", end)
