

from collections import defaultdict


class Solution:

    def max_level_sum_rec(self, cur, cur_level):
        result = defaultdict(int)
        if cur:
            result[cur_level] += cur.val
        if cur.left:
            left_result = self.max_level_sum_rec(cur.left, cur_level + 1)
            for k, v in left_result.items():
                result[k] += v
        if cur.right:
            right_result = self.max_level_sum_rec(cur.right, cur_level + 1)
            for k, v in right_result.items():
                result[k] += v

        return result

    def maxLevelSum(self, root: TreeNode) -> int:
        result = self.max_level_sum_rec(root, 1)
        print(result)
        return sorted(
            result.items(),
            key=lambda t: (t[1], -t[0]),
            reverse=True
        )[0][0]
