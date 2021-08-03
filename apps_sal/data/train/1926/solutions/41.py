import math


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        d = int(math.pow(num + 1, 0.5))
        e = int(math.pow(num + 2, 0.5))
        if (num == 1):
            return ([1, 2])
        ans = 24839749234923385
        ll = [-1, -1]
        for i in range(2, d + 1):
            if((num + 1) % i == 0):
                if (ans > ((num + 1) // i - i)):
                    ans = (num + 1) // i - i
                    ll = [i, (num + 1) // i]
        for i in range(2, e + 1):
            if((num + 2) % i == 0):
                if (ans > ((num + 2) // i - i)):
                    ans = (num + 2) // i - i
                    ll = [i, (num + 2) // i]

        return (ll)
