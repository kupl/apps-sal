class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if root:
            if d == 1:
                new_root = TreeNode(v)
                new_root.left = root

                return new_root

            queue = [root]
            level = 1
            while queue and level < d:
                row = []
                for i in range(len(queue)):
                    node = queue.pop(0)
                    if level == d - 1:
                        row.append(node)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                level += 1

            for node in row:
                old = node.left
                node.left = TreeNode(v)
                node.left.left = old

                old = node.right
                node.right = TreeNode(v)
                node.right.right = old

        return root
