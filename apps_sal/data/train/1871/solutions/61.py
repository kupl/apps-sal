
def calculateDifference(root, parent):
    maxi = 0
    for i in parent:
        if abs(root.val - i) > maxi:
            maxi = abs(root.val - i)
    if root.left:
        maxi = max(maxi, calculateDifference(root.left, parent + [root.val]))
    if root.right:
        maxi = max(maxi, calculateDifference(root.right, parent + [root.val]))

    return maxi


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return calculateDifference(root, [])
