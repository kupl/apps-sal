class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        if original == target:
            return cloned
        else:
            left = self.getTargetCopy(original.left, cloned.left, target)
            right = self.getTargetCopy(original.right, cloned.right, target)
        if left:
            return left
        else:
            return right
