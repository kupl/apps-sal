class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n == 1:
            return 1
        p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        if n < 98:
            lo, hi = 0, 24
            while lo <= hi:
                mid = (hi - lo) // 2 + lo
                if p[mid] == n:
                    idx = mid + 1
                    break
                elif p[mid - 1] < n and n < p[mid]:
                    idx = mid
                    break
                elif p[mid] > n:
                    hi = mid - 1
                else:
                    lo = mid + 1
        else:
            idx = 25

        # print(idx)

        p_prod = 1
        for i in range(1, idx + 1):
            p_prod = (p_prod * (i % 1000000007)) % 1000000007

        c_prod = 1
        for i in range(1, n - idx + 1):
            c_prod = (c_prod * (i % 1000000007)) % 1000000007

        return (p_prod * c_prod) % 1000000007
