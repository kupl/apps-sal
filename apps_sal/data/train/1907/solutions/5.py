class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not cloned:
            return None
        if cloned.val == target.val:
            return cloned
        return self.getTargetCopy(original, cloned.left, target) or self.getTargetCopy(original, cloned.right, target)
