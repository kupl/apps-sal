class Solution:

    def rob_node(self, node):
        if not node.left:
            (rob_node_left, not_rob_node_left) = (0, 0)
        else:
            (rob_node_left, not_rob_node_left) = self.rob_node(node.left)
        if not node.right:
            (rob_node_right, not_rob_node_right) = (0, 0)
        else:
            (rob_node_right, not_rob_node_right) = self.rob_node(node.right)
        return (node.val + not_rob_node_left + not_rob_node_right, max(rob_node_left, not_rob_node_left) + max(rob_node_right, not_rob_node_right))

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        (rob_root, not_rob_root) = self.rob_node(root)
        return max(rob_root, not_rob_root)
