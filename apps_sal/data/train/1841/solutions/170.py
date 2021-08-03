class Solution:
    def getStrongest(self, l: List[int], k: int) -> List[int]:
        l.sort()
        m = l[(len(l) - 1) // 2]

        def fun(a, b):
            if(abs(a - m) < abs(b - m)):
                return 1
            elif(abs(a - m) > abs(b - m)):
                return -1
            else:
                return -1
        l = sorted(l, key=cmp_to_key(fun))
        l1 = []
        for i in range(k):
            l1.append(l[i])
        return l1
