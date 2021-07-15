# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        store = {}
        
        def helper(node, level):
            if node:
                helper(node.left,level+1)
                helper(node.right,level+1)
                
                if level in store:
                    store[level].append(node.val)
                else:
                    store[level] = [node.val]
                    
                return node
            
        helper(root,1)
        
        for i in list(store.keys()):
            store[i] = sum(store[i])
            
        mx = sorted(list(store.items()), key=lambda x: (x[1]))
        return(mx[-1][0])
            
        

