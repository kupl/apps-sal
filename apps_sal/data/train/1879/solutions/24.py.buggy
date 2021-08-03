# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        \"\"\"
        (1) level-order
            replace until end then sum list
        \"\"\"
        q, deepest_sum = deque(), 0
        q.append(root)
        while len(q):
            i, deepest_sum = len(q), 0
            while i > 0:
                top = q.popleft()
                deepest_sum += top.val
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
                i -= 1
        return deepest_sum
            
