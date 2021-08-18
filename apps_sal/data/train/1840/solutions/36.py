class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.helper(root)
        l = [root]
        m = 0
        while len(l) != 0:
            node = l.pop()
            if node.left != None:
                l.append(node.left)
            if node.right != None:
                l.append(node.right)
            if max(node.val) > m:
                m = max(node.val)
        return m

    def helper(self, root):
        if root is None:
            return 0
        self.helper(root.left)
        self.helper(root.right)
        if root.left == None and root.right == None:
            root.val = (0, 0)
        elif root.left != None and root.right == None:
            root.val = (root.left.val[1] + 1, 0)
        elif root.right != None and root.left == None:
            root.val = (0, root.right.val[0] + 1)
        else:
            root.val = (root.left.val[1] + 1, root.right.val[0] + 1)
