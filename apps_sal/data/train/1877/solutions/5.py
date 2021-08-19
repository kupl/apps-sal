# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        sum_t_root = TreeNode(root.val)
        sum_t_node = sum_t_root
        t_node = root

        def calSumT(node, sum_t_node, s):
            if not node:
                return
            # print (node.val)
            if not node.left and not node.right:
                sum_t_node.val = True if s >= limit else False
            if node.left:
                sum_t_node.left = TreeNode(node.left.val + s)
                calSumT(node.left, sum_t_node.left, s + node.left.val)
            if node.right:
                sum_t_node.right = TreeNode(node.right.val + s)
                calSumT(node.right, sum_t_node.right, s + node.right.val)

        calSumT(t_node, sum_t_node, root.val)

        def strT(node):
            if not node:
                return []
            return [node.val] + strT(node.left) + strT(node.right)

        # print (strT(sum_t_root))

        def checkSumT(node):
            if not node.left and not node.right:
                return
            rtn = False
            if node.left:
                checkSumT(node.left)
                rtn |= node.left.val
            if node.right:
                checkSumT(node.right)
                rtn |= node.right.val
            node.val = rtn

        sum_t_node = sum_t_root
        checkSumT(sum_t_node)
        # print (strT(sum_t_root))

        def updateNode(node, s_node):
            if not node or not s_node.val:
                return None
            # print (node.val)
            if node.left:
                node.left = updateNode(node.left, s_node.left)
            if node.right:
                node.right = updateNode(node.right, s_node.right)
            return node

        return updateNode(root, sum_t_root)
