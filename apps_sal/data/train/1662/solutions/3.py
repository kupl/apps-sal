# Use a queue. Add root node, then loop:
# get first queue element, add all its children in the queue, left to right
# and add the current node's value in the result

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
