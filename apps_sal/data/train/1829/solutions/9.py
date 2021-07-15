# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = collections.deque([(root, root.val)])
        while q:
            node, cur_max = q.popleft()
            if node.val >= cur_max:
                res += 1
            for child in filter(bool, (node.left, node.right)):
                q.append((child, max(child.val, cur_max)))
        return res
