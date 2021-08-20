class Solution:

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        table = {}
        stack = [(root, [])]
        while stack:
            (node, path) = stack.pop()
            if not node:
                continue
            table.setdefault(len(path), []).append(path)
            stack.append((node.left, path + ['0']))
            stack.append((node.right, path + ['1']))
        maxwidth = 0
        for n in sorted(table):
            paths = table[n]
            if len(paths) < 1:
                continue
            if len(paths) == 1:
                maxwidth = max(1, maxwidth)
                continue
            values = list(map(lambda p: int(''.join(p), 2), paths))
            width = max(values) - min(values) + 1
            maxwidth = max(maxwidth, width)
        return maxwidth
