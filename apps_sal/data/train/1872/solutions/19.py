# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = 1
        count = 1
        bfs = [(root,level)]
        res = dict()
        while (len(bfs) >0):
            node, lvl = bfs[0]
            bfs.remove((node,lvl))
            if (res.get(lvl) == None):
                res[lvl] = 0
            res[lvl] += node.val
            if (node.left):
                bfs.append((node.left, lvl+1))
            if (node.right):
                bfs.append((node.right, lvl + 1))
        maxs = max(res.values())
        for i in list(res.keys()):
            if (res[i]==maxs):
                return i

