# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        
        def generateSumT(node, s):
            if not node: return (None, False)
            if not node.left and not node.right:
                if s >= limit: 
                    # print (\"valid leaf\", node.val, s)
                    return (node, True) 
                else: return (None, False)
                
            isValid = False
            if node.left:
                node.left, L = generateSumT(node.left, s+node.left.val)
                isValid |= L
            if node.right:
                node.right, R = generateSumT(node.right, s+node.right.val )
                isValid |= R
                
            if isValid:
                return (node, True)
            else:
                return (None, False)
        
        rtn, _ = generateSumT(root, root.val)
        
#         def strT(node):
#             if not node: return []
#             return [node.val]+strT(node.left)+strT(node.right)
        
#         print (strT(rtn))
        
#         def updateNode(node, s_node):
#             if not node or not s_node.val: return None
#             # print (node.val)
#             if node.left:
#                 node.left = updateNode(node.left, s_node.left)
#             if node.right:
#                 node.right = updateNode(node.right, s_node.right)
#             return node
        
        return rtn

