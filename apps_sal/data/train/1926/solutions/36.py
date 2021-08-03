class Solution:
    def closestDivisors(self, num: int) -> List[int]:

        def find_closest(cur):
            nonlocal mini
            nonlocal ans

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
        mini = float('inf')
        ans = None

        find_closest(num + 1)

        return ans
