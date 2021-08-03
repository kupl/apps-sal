def isTree(matrix):
    seen = [False] * len(matrix)

    def traverse(from_node, to_node):
        if not seen[to_node]:
            seen[to_node] = True
            for next_node in matrix[to_node]:
                if next_node != from_node:
                    if not traverse(to_node, next_node):
                        return False
            return True

    return traverse(None, 0) and all(seen)
