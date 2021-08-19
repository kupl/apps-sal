# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:

        q = collections.deque()
        res = 0
        q.append((root, 0, 0))

        while q:
            size = len(q)
            for _ in range(size):
                node, l, r = q.popleft()
                if node.left:
                    q.append((node.left, r + 1, 0))
                    res = max(res, r + 1)
                if node.right:
                    q.append((node.right, 0, l + 1))
                    res = max(res, l + 1)

        return res
