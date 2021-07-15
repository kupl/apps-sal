# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        if not root: return []
        q = deque()
        q.append((root, 0, 0))
        nodeset = []
        while q:
            node, x, y = q.popleft()
            nodeset.append((x, y, node.val))
            if node.left: q.append((node.left, x - 1, y + 1))
            if node.right: q.append((node.right, x + 1, y + 1))
        res = []
        nodeset.sort()
        x = nodeset[0][0] - 1
        for node in nodeset:
            if node[0] > x: 
                res.append([])
                x = node[0]
            res[-1].append(node[-1])
        return res
        
        
      
        
        
        
        
        
\"\"\"
        if not root: return []
        q = deque()
        q.append((root, 0, 0))
        res_l = []
        res_r = []
        while q:
            node, x, y = q.popleft()
            if node.left: q.append((node.left, x - 1, y + 1))
            if node.right: q.append((node.right, x + 1, y + 1))
            if x >= 0:
                if x == len(res_r): res_r.append([])
                res_r[x].append((y, node.val))
            else:
                x = - x - 1
                if x == len(res_l): res_l.append([])
                res_l[x].append((y, node.val))
        res = []
        for line in res_l[::-1] + res_r:
            res.append([val for _, val in sorted(line)])
        return res
\"\"\"        
        
        
        
        
        
        
        
\"\"\"
        if not root:
            return []
        nodeset = []
        queue = deque()
        queue.append((root, 0, 0))
        while queue:
            node, x, y = queue.popleft()
            nodeset.append((x, y, node.val))            
            if node.left:
                queue.append((node.left, x-1, y+1))
            if node.right:
                queue.append((node.right, x+1, y+1))
                
        nodeset = sorted(nodeset)
        res = {}
        for (x, y, val) in nodeset:
            if x not in res:
                res[x] = []
            res[x].append(val)
        return res.values()
\"\"\"
