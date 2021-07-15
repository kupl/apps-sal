# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        levels = collections.defaultdict(list)
        def move(node, lev, tl = None, ts = None):
            if node:
                levels[lev].append(node.val)
                
                
                if tl!=None and len(levels[tl]) == ts:
                    return node
                elif node.val==target.val:
                    return lev,len(levels[lev])
                
                left = move(node.left,lev+1, tl,ts)
                right = move(node.right,lev+1, tl,ts)
                
                return left or right
        
        
        tl,ts = move(original, 0)
        levels = collections.defaultdict(list)
        return move(cloned, 0, tl, ts)
