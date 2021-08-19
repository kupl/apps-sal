# a1, a2, a3, ... are the zombies numbers
# For a number x to be represented as a sum of those zombies, it means n-a1 or n-a2 or n-a3 or ... has to be represented
# From that, we can dynamically find if a number is representable (function "represent")
#
# an is the biggest zombie number
# If x is represented, then x + an is represented too
# Wich means we can divide numbers from 0 into groups of size an
# If the element i of a group is representable, then it will still be in the next group
#
# If the kth group is the same as the (k-1)th group, then it means no new number is representable
# In this case, there will be an infinite number of survivors
#
# If all number in the kth are representable, then it means the biggest non-representable number was in the previous group
# So we just find the biggest non-representable number of the previous group
#
# After an iterations of this, either we found there are infinites survivors
# Or we already filled the group (since they have a size of an)

from functools import lru_cache


def survivor(zombies):
    if not zombies:
        return -1
    nums = sorted(zombies)
    represent = lru_cache(maxsize=None)(lambda x: not x or any(represent(x - y) for y in nums[::-1] if x >= y))
    maxi = nums[-1]
    current = [0] * maxi
    for x in range(0, maxi**2, maxi):
        temp = [current[i] or represent(x + i) for i in range(maxi)]
        if temp == current:
            return -1
        if all(temp):
            y = next(i for i, v in enumerate(current[::-1]) if not v)
            return max(0, x - y - 1)
        current = temp
