import math


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def recurse(curr_n):
            if curr_n == 1:
                return []
            else:
                curr_arr = []
                init_val = '1/' + str(curr_n)
                curr_arr.append(init_val)
                for i in range(2, curr_n):
                    denom = str(curr_n)
                    if math.gcd(curr_n, i) == 1:
                        numer = str(i)
                        val = numer + '/' + denom
                        curr_arr.append(val)
                return curr_arr + recurse(curr_n - 1)

        return recurse(n)
