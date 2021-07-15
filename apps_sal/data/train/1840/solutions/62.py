class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def solve(root):
            if root:
                solve(root.left)
                solve(root.right)
                if root.left:d[root][0] = d[root.left][1] + 1
                if root.right:d[root][1] = d[root.right][0] + 1
                self.ans = max(self.ans,max(d[root]))
            return self.ans
        d = defaultdict(lambda:[0,0])
        self.ans = 0 
        solve(root)
        return self.ans
