class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        d = defaultdict(list)
        prev = ans = 0
        for r in reservedSeats:
            d[r[0]].append(r[1])
        for k in sorted(d):
            if k != prev + 1:
                ans += 2 * (k - prev - 1)
            prev = k
        if prev != n:
            ans += 2 * (n - prev)

        def get1row(x):
            if not x or all((i in [1, 10] for i in x)):
                return 2
            if all((i not in [4, 5, 6, 7] for i in x)) or all((i not in [2, 3, 4, 5] for i in x)) or all((i not in [6, 7, 8, 9] for i in x)):
                return 1
            return 0
        return ans + sum((get1row(d[k]) for k in d))
