s = list(input().strip())
t = input().strip()
sq = [int(a) for a in input().strip().split()]
l = len(s)
lt = len(t)


def check(x):
    tmp = s.copy()
    for i in range(x):
        tmp[sq[i] - 1] = '_'
    idx = 0
    for i in range(l):
        if tmp[i] == t[idx]:
            idx += 1
            if idx == lt:
                return True
    return False


low = res = 0
high = l
while(low <= high):
    mid = (low + high) >> 1
    if check(mid):
        low = mid + 1
        res = mid
    else:
        high = mid - 1
print(res)
