def isTree(matrix):
    (seen, stack) = (set(), [0])
    while stack:
        node = stack.pop()
        if node in seen:
            return False
        seen.add(node)
        stack += list(set(matrix[node]) - seen)
    return len(seen) == len(matrix)
