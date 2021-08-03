# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = deque([(root, 0)])
        res = defaultdict(list)
        while queue:
            top, l = queue.popleft()
            res[l].append(top.val)
            if top.left:
                queue.append((top.left, l + 1))
            if top.right:
                queue.append((top.right, l + 1))
        maxidx = max(sorted(res))
        return sum(res[maxidx])
