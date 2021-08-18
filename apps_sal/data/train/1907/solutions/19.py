
class Solution:

    def find(self, copy, target):

        if not copy:
            return None

        if copy.val == target:
            return copy

        a = self.find(copy.left, target)
        return a or self.find(copy.right, target)

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.find(cloned, target.val)
