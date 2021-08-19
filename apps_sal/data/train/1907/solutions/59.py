class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == target:
            return cloned
        elif original == None:
            return None
        else:
            left = self.getTargetCopy(original.left, cloned.left, target)
            right = self.getTargetCopy(original.right, cloned.right, target)
            if left != None:
                return left
            else:
                return right
