# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def solve(root, res, ind):
    if root == None:
        return 0
    l = solve(root.left, res, 0)
    r = solve(root.right, res, 1)
    if ind == 0:
        temp = 1 + r
    elif ind == 1:
        temp = 1 + l

    ans = 1 + max(l, r)
    res[0] = max(res[0], ans)
    return temp


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0

        res1 = [0]
        res2 = [0]
        c1 = solve(root, res1, 0)
        c2 = solve(root, res2, 1)
        # print(\"aa\",res1,res2,c1,c2)

        return max(res1[0], res2[0]) - 1
