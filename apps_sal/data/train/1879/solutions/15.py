class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

        stack = [(root, 0)]
        if not root:
            return 0
        leaf_nodes = []
        max_depth, deepest_sum = 0, 0
        while stack:
            node, depth = stack.pop()

            if depth > max_depth:
                max_depth = depth
                deepest_sum = node.val
            elif depth == max_depth:
                deepest_sum += node.val

            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))

        return deepest_sum
