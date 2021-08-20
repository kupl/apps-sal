class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        x_memo = collections.defaultdict(set)
        for (x, y) in points:
            x_memo[x].add(y)
        x_lst = sorted(list(x_memo.keys()))
        res = math.inf
        for i in range(len(x_lst)):
            for j in range(i + 1, len(x_lst)):
                dx = x_lst[j] - x_lst[i]
                y_common = x_memo[x_lst[i]].intersection(x_memo[x_lst[j]])
                if len(y_common) < 2:
                    continue
                y_common = sorted(list(y_common))
                for k in range(len(y_common) - 1):
                    res = min(res, dx * (y_common[k + 1] - y_common[k]))
        if math.isfinite(res):
            return res
        else:
            return 0
