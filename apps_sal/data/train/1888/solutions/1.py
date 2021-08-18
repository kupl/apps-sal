class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """

        if d == 1:
            newroot = TreeNode(v)
            newroot.left = root
            return newroot
        queue = [(root, 1)]
        for node, level in queue:
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
            if level == d - 1:
                newleft = TreeNode(v)
                newleft.left = node.left
                newright = TreeNode(v)
                newright.right = node.right
                node.left = newleft
                node.right = newright
        return root
