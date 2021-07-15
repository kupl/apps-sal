# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        lvl = 1
        sums = [[root.val, 1]]
        
        # apply bfs
        queue = [root]
        tmp = []
        lvl += 1
        while queue:
            node = queue.pop(0)
            if node.left is not None:
                tmp.append(node.left)
            if node.right is not None:
                tmp.append(node.right)
                
            if len(queue) == 0:
                res = 0
                for i in tmp:
                    queue.append(i)
                    res += i.val
                    
                if len(queue) != 0:
                    sums.append([res, lvl])
                tmp = []
                lvl += 1
                
        sums.sort(key = lambda x: x[0])
        return sums[-1][1]
