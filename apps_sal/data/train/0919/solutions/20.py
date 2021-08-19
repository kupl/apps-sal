import sys
sys.setrecursionlimit(1000000)


def LCES(l, prevSel, parity, ind, length):
    if(ind == len(l)):
        if(parity == 0):
            return length
        else:
            return -1
    else:
        if(parity == 0):
            # if(dp.get(str(parity)+" "+str(ind))):
            #     return dp[str(parity)+" "+str(ind)]
            left = LCES(l, l[ind], 1, ind + 1, length + 1)
            right = LCES(l, prevSel, 0, ind + 1, length)
            return max(left, right)
            # return dp[str(parity)+" "+str(ind)]
        else:
            if(prevSel != l[ind]):
                return LCES(l, prevSel, 1, ind + 1, length)
            else:
                left = LCES(l, l[ind], 0, ind + 1, length + 1)
                return left


for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    dp = {}
    left = LCES(l, l[0], 1, 1, 1)
    right = LCES(l, -1, 0, 1, 0)
    print(n - max(left, right))
