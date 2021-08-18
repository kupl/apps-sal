
class Solution:
    def getTargetCopy(self, o: TreeNode, c: TreeNode, t: TreeNode) -> TreeNode:
        if o == None:
            return
        if o == t:
            return c
        return self.getTargetCopy(o.left, c.left, t) or self.getTargetCopy(o.right, c.right, t)
