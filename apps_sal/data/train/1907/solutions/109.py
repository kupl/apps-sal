class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original or original == target:
            return cloned
        l = self.getTargetCopy(original.left, cloned.left, target)
        if l:
            return l
        r = self.getTargetCopy(original.right, cloned.right, target)
        if r:
            return r
