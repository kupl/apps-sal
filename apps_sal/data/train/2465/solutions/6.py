import math


class Solution:
    def divisorGame(self, N: int) -> bool:
        m = [0 for x in range(N + 1)]
        m[1] = 0
        for x in range(2, N + 1):
            temp = []
            i = 1
            while i < math.sqrt(x):
                if x % i == 0:
                    if x / i == i:
                        temp.append(i)
                    else:
                        temp.append(i)
                        if x / i != x:
                            temp.append(int(x / i))
                i += 1

            for y in temp:
                print(('x-y', x - y))
                if m[x - y] == 0:
                    m[x] = 1

        return True if m[N] == 1 else False
