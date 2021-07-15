from collections import deque

def tree_by_levels(node):
    if not node: return []
    queue = deque([node])
    level_order = []
    while queue:
        cur_node = queue.popleft()
        level_order.append(cur_node.value)
        if cur_node.left: queue.append(cur_node.left)
        if cur_node.right: queue.append(cur_node.right)
    return level_order
