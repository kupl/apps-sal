class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        self.memo = {}
        if not arr:
            return 0

        possible_values = []
        for column in range(len(arr[0])):
            possible_values.append(self.visit_row(arr, 0, column))

        return min(possible_values)

    def visit_row(self, arr, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        if i == len(arr) - 1:
            return arr[i][j]
        val = arr[i][j]
        possible_values = []
        prev_val = 999999999999999
        for k in [i[0] for i in sorted(enumerate(arr[i + 1]), key=lambda x:x[1])]:
            if k == j:
                continue
            next_val = self.visit_row(arr, i + 1, k)
            possible_values.append(next_val)
            if prev_val < next_val:
                break
            prev_val = next_val
        val += min(possible_values)
        self.memo[(i, j)] = val
        return val
