# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        
        def check(root):
            l = 0   #   以当前节点向左
            r = 0   #   以当前节点向右
            m = 0   #   当前子树的最大值(起点不一定是当前节点)
            if root.left != None:
                r1 = check(root.left)
                l = r1[1] + 1
                m = max(m, r1[2])
            if root.right!= None:
                r2 = check(root.right)
                r = r2[0] + 1
                m = max(m, r2[2])
            return (l, r, max(l, r, m))
        
        if root == None:
            return 0
        r = check(root)
        return r[2]
