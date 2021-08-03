import itertools


class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        nr, nc = len(arr), len(arr[0])
        for (r_i, c_i) in itertools.product(
            list(range(nr - 2, -1, -1)),
            list(range(nc))
        ):
            downs = [
                (r_i + 1, d_c) for d_c in range(nc) if d_c != c_i
            ]
            min_downs = min([
                arr[d_r][d_c] for (d_r, d_c) in downs
            ])

            arr[r_i][c_i] += min_downs

        return min([
            arr[0][c] for c in range(nc)
        ])
