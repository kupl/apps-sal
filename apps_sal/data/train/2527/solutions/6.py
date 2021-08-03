class Solution(object):

    def ca(self, a, b):
        s = [[] for i in range(a)]

        for i in range(b):
            s.append(0)
        return len(s)

    def cal(self, big, small):
        aa = [[] for i in range(big)]
        for i in range(small):
            aa.pop()
        return len(aa)

    def getSum(self, a, b):
        if a == 2147483647:
            return -1
        if a > 0 and b < 0:
            a, b = b, a

        if a == 0:
            return b
        if b == 0:
            return a

        if a < 0 and b < 0:
            return -self.ca(abs(a), abs(b))
        elif a > 0 and b > 0:
            return self.ca(a, b)

        elif a < 0 and b > 0:
            if abs(a) > b:
                return -self.cal(abs(a), b)
            elif abs(a) == b:
                return 0
            else:
                return self.cal(b, abs(a))
