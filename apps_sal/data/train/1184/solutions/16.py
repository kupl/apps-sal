from itertools import permutations as per
netsum = 0
try:
    for _ in range(int(input())):
        n = int(input())
        dic = {}
        for __ in range(n):
            a, b = input().split()
            if (a, b) not in dic:
                dic[(a, b)] = 1
            else:
                dic[(a, b)] += 1
        best = - (10**3)
        for p in list(per(['A', 'B', 'C', 'D'])):
            profit = 0
            lc = []
            for tup in zip(p, ['12', '3', '6', '9']):

                lc.append(dic.get(tup, 0))
                if lc[-1] == 0:
                    profit -= 100
            lc = sorted(lc)
            pr = 25
            for x in lc:
                profit += pr * x
                pr += 25

            best = max(best, profit)
        print(best)
        netsum += best
    print(netsum)
except:
    pass
