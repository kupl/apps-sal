# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        nodes=[[root]]
        for node in nodes:
            tmp=[]
            for n in node:
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            if tmp:
                nodes.append(tmp)
        nodes=[sum([n.val for n in node]) for node in nodes]
        return nodes.index(max(nodes))+1
