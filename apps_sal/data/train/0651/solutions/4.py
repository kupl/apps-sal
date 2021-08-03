def chk(n):
    return (n % 2)


def ans(n, dic):
    count = 0
    remain = 0
    for i in dic:
        if chk(dic[i]):
            count += 1
        else:
            remain += 1
    if chk(remain):
        count += remain - 1
    else:
        count += remain
    return count


t = int(input())
for w in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    dic = {}
    for i in arr:
        try:
            dic[i] += 1
        except:
            dic[i] = 1
    print(ans(n, dic))
