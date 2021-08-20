class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original.val == target.val:
            return cloned
        if original.left and original.right:
            return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)
        elif original.left and (not original.right):
            return self.getTargetCopy(original.left, cloned.left, target)
        elif original.right:
            return self.getTargetCopy(original.right, cloned.right, target)
        else:
            return None
