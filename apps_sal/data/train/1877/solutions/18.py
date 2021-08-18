
def collect_insufficient_nodes(node, cur_sum, nodes, limit):
    if node is None:
        return 0

    subpath_sums = []
    if node.left:
        subpath_sums.append(collect_insufficient_nodes(node.left, cur_sum + node.val, nodes, limit))
    if node.right:
        subpath_sums.append(collect_insufficient_nodes(node.right, cur_sum + node.val, nodes, limit))

    max_subpath_sum = 0 if not len(subpath_sums) else max(subpath_sums)

    if cur_sum + max_subpath_sum + node.val < limit:
        nodes.append(node)

    return max_subpath_sum + node.val


def delete_nodes(node, nodes):
    if not node:
        return

    if node.left in nodes:
        node.left = None
    else:
        delete_nodes(node.left, nodes)

    if node.right in nodes:
        node.right = None
    else:
        delete_nodes(node.right, nodes)


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        nodes = []
        collect_insufficient_nodes(root, 0, nodes, limit)
        nodes = set(nodes)
        if root in nodes:
            return None
        delete_nodes(root, nodes)
        return root
