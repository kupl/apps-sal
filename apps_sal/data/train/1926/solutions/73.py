class Solution:

    def closestDivisors(self, num: int) -> List[int]:

        def get_best_divisors(num):
            ans = [1, num]
            i = 2
            while i * i <= num:
                if num % i == 0:
                    divisor = num // i
                    if divisor - i < ans[1] - ans[0]:
                        ans = [i, divisor]
                i += 1
            return ans
        n_plus1_cand = get_best_divisors(num + 1)
        diff1 = n_plus1_cand[1] - n_plus1_cand[0]
        if diff1 == 0:
            return n_plus1_cand
        n_plus2_cand = get_best_divisors(num + 2)
        diff2 = n_plus2_cand[1] - n_plus2_cand[0]
        if diff2 < diff1:
            return n_plus2_cand
        return n_plus1_cand
