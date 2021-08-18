class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        stack = [(root, 0, 'left')]
        res = 0
        while stack:
            node, length, d = stack.pop()
            res = max(res, length)
            if node.left:
                if d != 'left':
                    stack.append((node.left, length + 1, 'left'))
                else:
                    stack.append((node.left, 1, 'left'))

            if node.right:
                if d != 'right':
                    stack.append((node.right, length + 1, 'right'))
                else:
                    stack.append((node.right, 1, 'right'))
        return res
