
class Solution:
    def sameTree(self, s, t):
        if not s or not t:
            return s == t
        return s.val == t.val and self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)

    def findTarget(self, s, target):
        if not s:
            return [s] if not target else []
        res = [s] if s.val == target.val else []
        return res + self.findTarget(s.left, target) + self.findTarget(s.right, target)

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        for l in self.findTarget(original, target):
            for r in self.findTarget(cloned, target):
                if self.sameTree(l, r):
                    return r
