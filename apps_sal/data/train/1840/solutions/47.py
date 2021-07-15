class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.maxpath = 0
        l, r = self.visit(root)
        return self.maxpath
    
    
    def visit(self, root):
        l = 0
        r = 0
        if root.left:
            ll,lr = self.visit(root.left)
            l = lr + 1
        if root.right:
            rl,rr = self.visit(root.right)
            r = rl + 1
        if max(l,r) > self.maxpath:
            self.maxpath = max(l,r)
        return l, r
