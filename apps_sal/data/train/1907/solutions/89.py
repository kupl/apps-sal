class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original or not cloned or (not target):
            return None
        if cloned.val == target.val:
            return cloned
        if self.getTargetCopy(original.left, cloned.left, target):
            return self.getTargetCopy(original.left, cloned.left, target)
        else:
            return self.getTargetCopy(original.right, cloned.right, target)
