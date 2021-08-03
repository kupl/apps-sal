# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if not root.left and not root.right:
            return root.val
        arr = [[root.val]]

        def helper(n, l):
            if not n:
                return
            if len(arr) < l + 1:
                arr.append([])
            arr[l].append(n.val)
            helper(n.left, l + 1)
            helper(n.right, l + 1)

        helper(root.left, 1)
        helper(root.right, 1)
        print(arr)
        res = -2**32 + 1
        ans = 1
        for j, i in enumerate(arr):
            if sum(i) > res:
                res = sum(i)
                ans = j + 1
        return ans
