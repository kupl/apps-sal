class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:

        if not root:
            return 0

        map_depth_sums = collections.defaultdict(int)

        max_level = 0
        max_sum = float(-inf)

        stack = [(root, 1)]

        while(stack):
            curr_node, level = stack.pop()
            map_depth_sums[level] += curr_node.val

            if curr_node.right:
                stack.append((curr_node.right, level + 1))
            if curr_node.left:
                stack.append((curr_node.left, level + 1))

        level = 1
        while(level in map_depth_sums):
            if map_depth_sums[level] > max_sum:
                max_sum = map_depth_sums[level]
                max_level = level
            level += 1

        return max_level
