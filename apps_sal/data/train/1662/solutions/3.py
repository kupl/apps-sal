def tree_by_levels(node):
    queue = []
    result = []
    if node == None:
        return result
    queue.append(node)
    while len(queue) > 0:
        n = queue.pop(0)
        if n.left != None:
            queue.append(n.left)
        if n.right != None:
            queue.append(n.right)
        result.append(n.value)
    return result
