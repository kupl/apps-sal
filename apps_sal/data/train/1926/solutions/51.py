class Solution:
    def closestDivisors(self, num: int) -> List[int]:

        mini = float('inf')
        ans = None

        cur = num + 1

        y = int(sqrt(cur + 2))
        flag = False
        while y * y >= 1:
            mod = cur % y
            if(not mod):
                other = cur // y
                if((other - y) < mini):
                    mini = other - y
                    ans = [y, other]
                    flag = True
            elif((mod + 1) == y):
                other = (cur + 1) // y
                if((other - y) < mini):
                    mini = other - y
                    ans = [y, other]
                    flag = True
            y -= 1
            if(flag):
                break

        return ans
