class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        s = 1
        a = [[root, 1]]
        while 1:
            b = []
            for p in a:
                if p[0].left:
                    b.append([p[0].left, 2 * p[1] - 1])
                if p[0].right:
                    b.append([p[0].right, 2 * p[1]])
            a = b
            if a:
                s = max(s, a[-1][1] - a[0][1] + 1)
            else:
                break
        return s
