class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned is None:
            return -1
        if cloned.val == target.val:
            return cloned
        left = self.getTargetCopy(original, cloned.left, target)
        if left != -1:
            return left
        return self.getTargetCopy(original, cloned.right, target)
