from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        bfs = defaultdict(list)
        
        def traverse(head, n):
            if head is None:
                return
            bfs[n].append(head.val)
            traverse(head.left, n+1)
            traverse(head.right, n+1)
        
        traverse(root, 1)
        
        s=-9999
        l=0
        for i in bfs:
            bfs[i]=sum(bfs[i])
            if bfs[i]>s:
                s=bfs[i]
                l=i
        return l
