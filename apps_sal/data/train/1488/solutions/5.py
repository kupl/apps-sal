def cal(a, count, k, poss, ind):
    temp = a.copy()
    if len(poss) == 0:
        for i in range(1, len(a)):
            if temp[i] > temp[i - 1]:
                k -= 1
        if k == 0 and 0 not in temp:
            count += 1
        return count
    if temp[ind] == 0:
        for item in poss:
            temp[ind] = item
            count = cal(temp, count, k, poss - set([item]), ind + 1)
    else:
        count = cal(temp, count, k, poss, ind + 1)
    return count


t = int(input())
while t > 0:
    t -= 1
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    poss = set()
    for i in range(1, len(a) + 1):
        if i not in a:
            poss.add(i)
    count = cal(a, 0, k, poss, 0)
    print(count)
