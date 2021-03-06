class Solution:

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = -1

        def solve(r: TreeNode, ancestors: List[int]):
            if r is None:
                return
            v = r.val
            if len(ancestors) > 0:
                tmp = max([abs(a - v) for a in ancestors])
                self.ans = max(tmp, self.ans)
            ancestors.append(v)
            solve(r.left, ancestors)
            solve(r.right, ancestors)
            ancestors.pop()
        solve(root, [])
        return self.ans
