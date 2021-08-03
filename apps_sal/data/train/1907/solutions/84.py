# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def getpath(node1, node2):
            if node1.val == node2.val:
                return node1
            get_l = -1
            get_r = -1
            if (node1.left is not None):
                get_l = getpath(node1.left, node2)
                if get_l != -1:
                    return get_l
            if (node1.right is not None):
                get_r = getpath(node1.right, node2)
                if get_r != -1:
                    return get_r
                return -1
            if get_l == -1 and get_r == -1:
                return -1
        return getpath(cloned, target)
