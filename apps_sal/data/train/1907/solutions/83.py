# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        nonlocal target_c,stack_o,stack_c
        target_c=None
        stack_o=[original]
        stack_c=[cloned]
        def helper():
            nonlocal target_c
            if(len(stack_o)<=0):
                return
            current_node_o=stack_o.pop()
            current_node_c=stack_c.pop()
            if(current_node_o==None):
                helper()
                return
            if(current_node_o.val==target.val):
                target_c=current_node_c
            stack_o.append(current_node_o.left)
            stack_c.append(current_node_c.left)
            stack_o.append(current_node_o.right)
            stack_c.append(current_node_c.right)
            helper()
            #helper(node_o.right,node_c.right)
        helper()
        #print(target_c)
        return target_c

