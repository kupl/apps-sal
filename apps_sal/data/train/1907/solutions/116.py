class Solution:

    def getTargetCopy(self, p: TreeNode, q: TreeNode, target: TreeNode) -> TreeNode:
        if not p and (not q):
            return
        if p == target:
            return q
        return self.getTargetCopy(p.left, q.left, target) or self.getTargetCopy(p.right, q.right, target)
