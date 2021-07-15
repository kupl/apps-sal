# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


##### Stack DFS solution
# class Solution:
    
#     def deepestLeavesSum(self, root: TreeNode) -> int:

#         def isLeaf(node) -> bool:
#             return node.left is None and node.right is None

#         deepest_sum = 0
#         depth = 0
        
#         # Push root into stack
#         stack = [(root, 0)]
#         # while stack is not empty
#         while stack:
#             # Pop out a node from the stack and update the current number
#             node, current_depth = stack.pop()
#             # If the node is a leaf
#             if isLeaf(node):
#                 # Update the deepest leaves sum deepest_sum
                
#                 # If we are at a deeper level                
#                 if depth < current_depth:
#                     deepest_sum = node.val # start a new sum
#                     depth = current_depth # note new depth
                
#                 elif depth == current_depth:
#                     deepest_sum += node.val # update existing sum
                    
#             else:
#             # Push right and left child nodes into stack (right first)
#                 if node.right:
#                     stack.append((node.right, current_depth + 1))
#                 if node.left:
#                     stack.append((node.left, current_depth + 1))
#         return deepest_sum
        
    
# Queue BFS Solution
class Solution:
    
    def deepestLeavesSum(self, root: TreeNode) -> int:


        
        next_level = deque([root,])
        
        while next_level:
            # prepare for the next level
            curr_level = next_level
            next_level = deque()
            
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        
        return sum([node.val for node in curr_level])
