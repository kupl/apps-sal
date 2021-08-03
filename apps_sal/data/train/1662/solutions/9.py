from collections import deque


def tree_by_levels(node):
    q, result = deque(), []
    if node is not None:
        q.append(node)
    while len(q):
        node = q.popleft()
        result.append(node.value)
        q.extend(i for i in (node.left, node.right) if i is not None)
    return result
