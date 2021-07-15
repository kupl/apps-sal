# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    - as we traverse down, we measure the maxSoFar and compare current 
    node with that
    - current node is good if >= maxSoFar, so count as one
    - can traverse recursively
    '''
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node, maxSoFar=float(\"-inf\")):
            # check base case (null node)
            if not node:
                return 0
            
            # process node
            count = 1 if node.val >= maxSoFar else 0
            maxSoFar = max(maxSoFar, node.val)
            
            # traverse children, adding count along the way
            return traverse(node.left, maxSoFar) + traverse(node.right, maxSoFar) + count
            
        if not root:
            return 0
        return traverse(root)
        
        
