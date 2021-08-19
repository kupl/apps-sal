def isTree(matrix):
    """depth first search; tree on n vertices has exactly n-1 edges"""
    vertices = set(range(len(matrix)))
    stack = [vertices.pop()]
    while stack:
        children = {y for y in matrix[stack.pop()] if y in vertices}
        vertices.difference_update(children)
        stack.extend(children)
    return not vertices and sum(map(len, matrix)) == 2 * len(matrix) - 2
