import math


def difun(num):
    ans = num
    n1 = 0
    n2 = 0
    for i in range(int(math.sqrt(num)), 0, -1):
        abc = abs(i - (num // i))
        if(num % i == 0 and abc < ans):
            ans = abc
            n1 = i
            n2 = num // i
    return ans, n1, n2


class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        a, b, c = difun(num + 1)
        print(a, b, c)
        d, e, f = difun(num + 2)
        print(d, e, f)
        if(a < d):
            return [b, c]
        return [e, f]
