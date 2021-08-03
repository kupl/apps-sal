class Solution:\r
    def circularPermutation(self, n: int, start: int) -> List[int]:\r
        result = list(range(1 << n))\r
\r
        def reverse(lst, i, j):\r
            while i < j:\r
                lst[i], lst[j] = lst[j], lst[i]\r
                i, j = i + 1, j - 1\r
\r
        for i in range(1, n):\r
            for j in range(1, (1 << (n - i)) + 1, 2):\r
                reverse(result, j << i, ((j + 1) << i) - 1)\r
\r
        start_idx = result.index(start)\r
        result = result[start_idx: 1 << n] + result[0: start_idx]\r
        return result
