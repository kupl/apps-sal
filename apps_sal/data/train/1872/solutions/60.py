# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        #bfs
        
        q = [root]
        sums = []
        while len(q)>0 :
            s = len(q)
            tmp = 0
            for i in range(s) :
                n = q.pop(0)
                tmp += n.val
                if n.left :
                    q.append(n.left)
                if n.right :
                    q.append(n.right)
                    
            sums.append(tmp)
        
        print(sums)
        level_sums = sorted(zip(range(len(sums)), sums), key=lambda x : (-x[1], x[0]))
        return level_sums[0][0]+1
