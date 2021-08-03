# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        sums,ans={},[float(\"inf\"),float(\"-inf\")]
        def traverse(root,lvl):
            if root:
                if lvl not in sums: sums[lvl]=0
                sums[lvl]+=root.val
                traverse(root.left,lvl+1)
                traverse(root.right,lvl+1)
        traverse(root,1)
        return sorted(sums.items(),key=lambda x: (-x[1],x[0]))[0][0]
