class Solution:

    def maxAncestorDiff(self, root: TreeNode) -> int:
        q = [(root, [])]
        from collections import defaultdict
        anc = {}
        while q:
            (cur, path) = q.pop(0)
            anc[cur.val] = path[:]
            path.append(cur.val)
            if cur.left:
                q.append((cur.left, path[:]))
            if cur.right:
                q.append((cur.right, path[:]))
        max_diff = float('-inf')
        for (n, ancs) in list(anc.items()):
            for a in ancs:
                max_diff = max(max_diff, abs(a - n))
        return max_diff
