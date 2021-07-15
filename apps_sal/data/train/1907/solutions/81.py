# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy1(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node, lst):
            if node:
                lst.append(node)
                dfs(node.left, lst)
                dfs(node.right, lst)
         
        original_stack, cloned_stack = [], []
        dfs(original, original_stack)
        dfs(cloned, cloned_stack)
        
        for l1, l2 in zip(original_stack, cloned_stack):
            if l1 == target:
                return l2
    
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # if original == target:
        #     return cloned
        # stack = [(original, cloned)]
        # while stack:
        #     node1, node2 = stack.pop()
        #     if node1 == target:
        #         return node2
        #     if node1.right:
        #         stack.append((node1.right, node2.right))
        #     if node1.left:
        #         stack.append((node1.left, node2.left))
        def it(node):
            if node:
                yield node
                yield from it(node.left)
                yield from it(node.right)
            
        for n1, n2 in zip(it(original), it(cloned)):
            if n1 == target:
                return n2
