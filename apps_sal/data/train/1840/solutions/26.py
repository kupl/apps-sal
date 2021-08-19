class Solution:

    def longestZigZag(self, root: TreeNode) -> int:
        q = collections.deque()
        res = 0
        q.append((root, 0, 0))
        while q:
            size = len(q)
            for _ in range(size):
                (node, l, r) = q.popleft()
                if node.left:
                    q.append((node.left, r + 1, 0))
                    res = max(res, r + 1)
                if node.right:
                    q.append((node.right, 0, l + 1))
                    res = max(res, l + 1)
        return res
