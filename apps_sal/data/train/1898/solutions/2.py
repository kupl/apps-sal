# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def merge(self, root, left, right):
        replace_left = replace_right = None
        for i in range(len(left)):
            if left[i] == root.left:
                replace_left = i
                
        for i in range(len(right)):
            if right[i] == root.right:
                replace_right = i
                
        if replace_left is not None and replace_right is None:
            left[replace_left] = root
            return left + right
        elif replace_right is not None and replace_left is None:
            right[replace_right] = root
            return left + right
        
        result = (
            [node for node in left if node != root.left] + 
            [node for node in right if node != root.right]
        )
        result.append(root)
        return result
    
    def helper(self, root, to_delete):
        if not root:
            return []
        if not root.left and not root.right:
            if root.val in to_delete:
                return []
            return [root]
        
        left = self.delNodes(root.left, to_delete)
        right = self.delNodes(root.right, to_delete)
        
        if root.left and root.left.val in to_delete:
            root.left = None
            
        if root.right and root.right.val in to_delete:
            root.right = None
        
        if root.val in to_delete:
            return left + right
        
        return self.merge(root, left, right)
            
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        return self.helper(root, set(to_delete))
            
        
            

