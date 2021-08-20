def isTree(matrix):
    visited = [False] * len(matrix)

    def traverse(origin, transit):
        if not visited[transit]:
            visited[transit] = True
            return all((traverse(transit, destination) for destination in matrix[transit] if destination != origin))
    return traverse(None, 0) and all(visited)
