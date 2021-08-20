class Solution:

    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque()
        max_depth = 0
        if root.left:
            q.append((root.left, True, 1))
        if root.right:
            q.append((root.right, False, 1))
        while q:
            (n, is_left, depth) = q.popleft()
            max_depth = max(depth, max_depth)
            if n.left:
                if is_left:
                    q.append((n.left, True, 1))
                else:
                    q.append((n.left, True, depth + 1))
            if n.right:
                if is_left:
                    q.append((n.right, False, depth + 1))
                else:
                    q.append((n.right, False, 1))
        return max_depth
