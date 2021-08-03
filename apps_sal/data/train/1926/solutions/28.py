from math import sqrt, ceil


class Solution:
    def closestDivisors(self, num):
        closeDivs = []
        closeDivDiff = 10000000000

        if int(sqrt(num + 1)) == sqrt(num + 1):
            sqrtNum = int(sqrt(num + 1))
            return [sqrtNum, sqrtNum]
        elif int(sqrt(num + 2)) == sqrt(num + 2):
            sqrtNum = int(sqrt(num + 2))
            return [sqrtNum, sqrtNum]

        num += 1
        for i in range(1, ceil(sqrt(num))):
            if num % i == 0 and int(num / i) - i < closeDivDiff:
                closeDivDiff = int(num / i) - i
                closeDivs = [i, int(num / i)]

        num += 1
        for i in range(1, ceil(sqrt(num))):
            if i == 19284:
                print('Yes')
            if num % i == 0 and int(num / i) - i < closeDivDiff:
                closeDivDiff = int(num / i)
                closeDivs = [i, int(num / i)]

        return closeDivs
