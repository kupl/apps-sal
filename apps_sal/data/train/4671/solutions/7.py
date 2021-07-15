from collections import defaultdict

def isTree(matrix):
    graph = defaultdict(set)
    for node, connections in enumerate(matrix):
        if not connections:
            return False
        for connection in connections:
            graph[connection].add(node)
            graph[node].add(connection)
            
    N = len(matrix)
    for node in graph.keys():
        stack, seen = [node], set()
        while stack:
            cur_node = stack.pop()
            if cur_node in seen:
                return False
            seen.add(cur_node)
            for next_node in graph[cur_node]:
                if next_node not in seen:
                    stack.append(next_node)
        if len(seen) < N:
            return False
    return True
