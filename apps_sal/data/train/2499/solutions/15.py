def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


class Solution:

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = list(collections.Counter(deck).values())
        list1 = list(count)
        mi = list1[0]
        for c in list1[1:]:
            mi = gcd(mi, c)
        if mi < 2:
            return False
        for i in count:
            if i % mi != 0:
                return False
        return True
