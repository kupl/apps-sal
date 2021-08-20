class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        a = sorted(A)
        b = []
        if a == sorted(set(a)):
            return 0
        res = 0
        for i in range(0, len(a) - 1):
            print('now: ', a[i], a[i + 1])
            if a[i + 1] == a[i]:
                a[i + 1] += 1
                res += 1
            elif a[i + 1] < a[i]:
                k = a[i] - a[i + 1] + 1
                a[i + 1] += k
                res += k
        print(b)
        return res
