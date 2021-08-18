from collections import defaultdict

for t in range(int(input())):
    n = int(input())
    s = input()
    d = defaultdict(int)
    for i in s:
        d[i] += 1
    count = 0
    for i, j in d.items():
        if j % 2 == 1:
            count += 1
    if (n // 2) % 2 == 0:
        if count == 0:
            print("YES")
        else:
            print("NO")
    else:
        if count == 2 or count == 0:
            print("YES")
        else:
            print("NO")
