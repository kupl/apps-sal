class Solution:

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        (nl, nh) = (len(str(low)), len(str(high)))
        ans = []
        sequential = '123456789'
        for n in range(nl, min(nh + 1, 10)):
            (start, delta) = (int(sequential[:n]), int('1' * n))
            k_min = 0 if n > nl else max(-(-(low - start) // delta), 0)
            k_max = 9 - n if n < nh else (min(high, int(sequential[-n:])) - start) // delta
            ans += [start + k * delta for k in range(k_min, k_max + 1)]
        return ans
