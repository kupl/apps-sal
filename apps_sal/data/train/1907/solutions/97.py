class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        if original.val == target.val:
            return cloned
        leftRes = self.getTargetCopy(original.left, cloned.left, target)
        if leftRes:
            return leftRes
        rightRes = self.getTargetCopy(original.right, cloned.right, target)
        if rightRes:
            return rightRes
