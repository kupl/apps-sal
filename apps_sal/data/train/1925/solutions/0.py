# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # time O(n); space O(n)
        vals = deque(preorder)

        def build(min_val, max_val):
            if vals and min_val < vals[0] < max_val:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(min_val, val)
                node.right = build(val, max_val)

                return node

        return build(float('-inf'), float('inf'))
