# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        ans = []
        def helper(node, isRoot, parent, p_left):
            if isRoot:
                ans.append(node)
                
            if node.val in to_delete:
                if isRoot:
                    ans.pop()
                if parent:
                    if p_left:
                        parent.left = None
                    else:
                        parent.right = None
                if node.left:                    
                    helper(node.left, True, node, True)
                if node.right:                    
                    helper(node.right, True, node, False)
            else:
                if node.left:
                    helper(node.left, False, node, True)
                if node.right:
                    helper(node.right, False, node, False)
                    
            return
        
        helper(root, True, None, None)
        return ans
                    
            
            
            
            
            
            
            
            
            
            
#             if node.val in to_delete:
#                 if node.left:
#                     ans.append(node.left)
#                     helper(node.left)
#                 if node.right:
#                     ans.append(node.right)
#                     helper(node.right)
#                 ans.pop()
#                 to_delete.remove(node.val)
                
#             if node.left and node.left.val in to_delete:
#                 node.left = None
#             if node.right and node.right.val in to_delete:
#                 node.right = None
                
#             return
#         helper(root)
#         return ans

