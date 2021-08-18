
class Solution:
    def getResult(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if (original == None) or (cloned == None) or (target == None):
            return None
        if (original.val == target.val):
            return cloned
        left_result = self.getResult(original.left, cloned.left, target)
        if (left_result):
            return left_result
        right_result = self.getResult(original.right, cloned.right, target)
        if (right_result):
            return right_result
        return None

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        result = self.getResult(original, cloned, target)
        return result
