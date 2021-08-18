
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original is None:
            return None
        if original == target:
            return cloned
        l = self.getTargetCopy(original.left, cloned.left, target)
        r = self.getTargetCopy(original.right, cloned.right, target)
        return l if l else r
