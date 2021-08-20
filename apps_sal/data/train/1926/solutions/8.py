class Solution(object):

    def closestDivisors(self, num):

        def fun(n):
            for i in range(int(n ** 0.5), 0, -1):
                if n % i == 0:
                    return [n // i, i]
        n1 = fun(num + 1)
        n2 = fun(num + 2)
        if abs(n2[1] - n2[0]) > abs(n1[1] - n1[0]):
            return n1
        return n2
