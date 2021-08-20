class Solution:

    def closestDivisors(self, num: int) -> List[int]:

        def find_closest(cur):
            nonlocal mini
            nonlocal ans
            y = 1
            while y * y <= cur + 2:
                mod = cur % y
                if not mod:
                    other = cur // y
                    if other - y < mini:
                        mini = other - y
                        ans = [y, other]
                elif mod + 1 == y:
                    other = (cur + 1) // y
                    if other - y < mini:
                        mini = other - y
                        ans = [y, other]
                y += 1
        mini = float('inf')
        ans = None
        find_closest(num + 1)
        return ans
