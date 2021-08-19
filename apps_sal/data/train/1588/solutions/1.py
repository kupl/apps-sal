from collections import defaultdict


def call_value():
    return 0


t = int(input())
while t > 0:
    n = int(input())
    arr = []
    for _ in range(n):
        (s, m) = input().split()
        m = int(m)
        arr.append([s, m])
    dic = defaultdict(call_value)
    for i in arr:
        dic[i[1]] += 1
    ans = []
    for i in dic:
        if dic[i] == 1:
            ans.append(i)
    if len(ans) == 0:
        print('Nobody wins.')
    else:
        mini = min(ans)
        for i in arr:
            if i[1] == mini:
                print(i[0])
                break
    t -= 1
