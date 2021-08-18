
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == target:
            return cloned

        if original.left:
            left = self.getTargetCopy(original.left, cloned.left, target)
            if left:
                return left

        if original.right:
            right = self.getTargetCopy(original.right, cloned.right, target)
            if right:
                return right

        return None
