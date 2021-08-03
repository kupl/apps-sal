# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque([(root, 1)])
        res = defaultdict(int)
        while q:
            n, l = q.popleft()
            res[l] += n.val
            if n.left:
                q.append((n.left, l + 1))
            if n.right:
                q.append((n.right, l + 1))
        argmax = 1
        vmax = root.val
        for k, v in list(res.items()):
            if v > vmax:
                argmax = k
                vmax = v
        return argmax
