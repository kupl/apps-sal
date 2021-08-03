from operator import itemgetter
n = int(input())
abi = [[-10**9, 0]] + [list(map(int, input().split())) for i in range(n)]
abi.sort(key=itemgetter(0))
ar = [0] * (n + 1)
ar[0] = 0


def check(pos, num):
    # print(pos,num)
    if abi[pos][0] < num:
        return True
    else:
        return False


def binsearch(num):
    high = n + 1
    low = 0
    mid = (high + low) // 2
    while high >= low:
        if check(mid, num):
            low = mid + 1
        else:
            high = mid - 1
        mid = (high + low) // 2
    return mid


ans = n
for i in range(1, n + 1):
    num = binsearch(abi[i][0] - abi[i][1])
    ar[i] = i - num - 1 + ar[num]
    ans = min(ans, ar[i] + n - i)
print(ans)
