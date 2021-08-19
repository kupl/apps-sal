class Solution:

    def longestZigZag(self, root: TreeNode) -> int:
        memo = dict()

        def zig_zag_len(node, direction):
            if not node:
                return -1
            if (node, direction) in memo:
                return memo[node, direction]
            if direction == 'L':
                memo[node, direction] = 1 + zig_zag_len(node.right, 'R')
            elif direction == 'R':
                memo[node, direction] = 1 + zig_zag_len(node.left, 'L')
            else:
                memo[node, direction] = max(1 + zig_zag_len(node.right, 'R'), 1 + zig_zag_len(node.left, 'L'), zig_zag_len(node.right, 'N'), zig_zag_len(node.left, 'N'))
            return memo[node, direction]
        return zig_zag_len(root, 'N')
