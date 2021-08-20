class Solution:

    def find(self, copy, target):
        if copy:
            if copy.val == target:
                return copy
            a = self.find(copy.left, target)
            return a if a else self.find(copy.right, target)
        return None

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.find(cloned, target.val)
