def findMaxDiff(node, collected):
    if not node:
        return float('-inf')
    cur_max = 0
    for v in collected:
        cur_max = max(cur_max, abs(v - node.val))
    left_max = findMaxDiff(node.left, collected + [node.val])
    right_max = findMaxDiff(node.right, collected + [node.val])
    return max(cur_max, left_max, right_max)


class Solution:

    def maxAncestorDiff(self, root: TreeNode) -> int:
        return findMaxDiff(root, [])
