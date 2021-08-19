class Solution:

    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        multiple = math.floor(math.log10(n))
        subtract = sum([math.pow(10, i) for i in range(0, multiple)])
        boundary = multiple * math.pow(10, multiple) - subtract
        diff = n - boundary
        if diff > 0:
            x = math.pow(10, multiple) - 1 + math.ceil(diff / (multiple + 1))
            p = (diff - 1) % (multiple + 1)
        elif diff <= 0:
            x = math.pow(10, multiple) + math.ceil(diff / multiple) - 1
            p = (diff - 1) % multiple
        r = [ch for ch in str(x)][int(p)]
        return int(r)
