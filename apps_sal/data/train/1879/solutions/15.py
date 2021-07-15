# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        stack=[(root,0)]
        if not root:return 0
        leaf_nodes=[]
        max_depth,deepest_sum=0,0
        while stack:
            node,depth=stack.pop()
            
            if depth>max_depth:
                max_depth=depth
                deepest_sum=node.val
            elif depth==max_depth:
                deepest_sum+=node.val
            
            if node.right:
                stack.append((node.right,depth+1))
            if node.left:
                stack.append((node.left,depth+1))
                
        
        return deepest_sum
        
#         stack=[(root,0)]
#         if not root:return 0
#         leaf_nodes=[]
#         max_depth=0
#         while stack:
#             node,depth=stack.pop()
#             max_depth=max(max_depth,depth)
#             if not node.left and not node.right:
#                 leaf_nodes.append((node.val,depth))
            
#             if node.right:
#                 stack.append((node.right,depth+1))
#             if node.left:
#                 stack.append((node.left,depth+1))
                
#         sum_=0
#         for vals,depth in leaf_nodes:
#             if depth==max_depth:
#                 sum_+=vals
#         return sum_
                
        
                
            

