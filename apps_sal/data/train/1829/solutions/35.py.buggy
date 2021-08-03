# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        \"\"\"
        count # of nodes >= root.val
        
        create a path from root to current node.
        
        a good node if all the nodes in the path are smaller than the current node
        
        this is a good example:
        [2,null,4,10,8,null,null,4]
        
        \"\"\"
        
        # the root nodes is always good node
        # so it start from 1
        self.numGoodNodes = 1
        def dfsVisit(node, path):
            if node is None:
                return
            
            if len(path) > 0 and node.val >= max(path):
                self.numGoodNodes += 1 
                
            dfsVisit(node.left, path + [node.val])
            dfsVisit(node.right, path + [node.val])
        
        dfsVisit(root, [])
                
        return self.numGoodNodes
