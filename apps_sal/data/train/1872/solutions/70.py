class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:

        def get_level_sums(root: TreeNode, level: int, level_sums: dict):
            if not root:
                return
            if level not in list(level_sums.keys()):
                level_sums[level] = root.val
            else:
                level_sums[level] += root.val
            get_level_sums(root.left, level + 1, level_sums)
            get_level_sums(root.right, level + 1, level_sums)
        if not root:
            return 0
        level_sums = {}
        get_level_sums(root, 1, level_sums)
        print(level_sums)
        max_key = 0
        max_value = min(level_sums.values())
        for k in list(level_sums.keys()):
            if level_sums[k] > max_value:
                max_key = k
                max_value = level_sums[k]
        return max_key
