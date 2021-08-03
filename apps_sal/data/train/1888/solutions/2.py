class Solution:

    def traverse_left(self, stack, node, node_depth, d):
        while node_depth + 1 < d and node.left is not None:
            stack.append((node.left, node_depth + 1))
            node = node.left
            node_depth += 1

    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """

        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root

        stack = [(root, 1)]
        self.traverse_left(stack, root, 1, d)

        while not (not stack):
            node, node_depth = stack.pop()
            if node_depth + 1 < d and node.right is not None:
                stack.append((node.right, node_depth + 1))
                self.traverse_left(stack, node.right, node_depth + 1, d)

            if node_depth == d - 1:
                a = TreeNode(v)
                a.left = node.left
                node.left = a
                b = TreeNode(v)
                b.right = node.right
                node.right = b

        return root
