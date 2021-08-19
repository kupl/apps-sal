from collections import OrderedDict
for i in range(int(input())):
    N = int(input())
    dic = OrderedDict()
    for i in range(N):
        (n, m) = list(input().split())
        if n in dic:
            if m == '1':
                dic[n][1] += 1
            else:
                dic[n][0] += 1
        elif m == '1':
            dic[n] = [0, 1]
        else:
            dic[n] = [1, 0]
    count = 0
    for (k, v) in dic.items():
        count += max(v[0], v[1])
    print(count)
