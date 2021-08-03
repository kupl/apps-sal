# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        ans = [-1]

        def aux(root, isleft, ans):
            if not root:
                return -1
            left = aux(root.left, 1, ans) + 1
            right = aux(root.right, 0, ans) + 1
            ans[0] = max(ans[0], left, right)
            if isleft:
                return right
            else:
                return left

        if not root:
            return 0
        aux(root, 0, ans)
        return ans[0]

#         def aux(root, isleft, memo):
#             if not root:
#                 return 0
#             if root in memo:
#                 if isleft:
#                     return memo[root][1]
#                 else:
#                     return memo[root][0]
#             memo[root] = [0, 0]
#             memo[root][0] = aux(root.left, 1, memo) + 1
#             memo[root][1] = aux(root.right, 0, memo) + 1
#             self.ans = max(self.ans, memo[root][1], memo[root][0])
#             if isleft:
#                 return memo[root][1]
#             else:
#                 return memo[root][0]

#         if not root:
#             return 0
#         memo = {}
#         aux(root, 0, memo)
#         return self.ans - 1
