class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        n = int(math.sqrt(num + 2))
        max_ = 0
        check = False
        for i in range(1, n + 1):
            if (num + 1) % i == 0:
                max_ = i
                check = False
            elif (num + 2) % i == 0:
                print(i)
                max_ = i
                check = True
        if check:
            return (max_, int((num + 2) / max_))
        else:
            return (max_, int((num + 1) / max_))
