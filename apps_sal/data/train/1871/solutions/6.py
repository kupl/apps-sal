def maxDiff(root, arr):
    a = 0
    for i in arr:
        a = max(a, abs(i - root.val))
    b = 0
    c = 0
    if (root.left):
        b = maxDiff(root.left, arr + [root.val])
    if (root.right):
        c = maxDiff(root.right, arr + [root.val])
    return max(a, b, c)


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return maxDiff(root, [])
