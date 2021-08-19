from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    ls = [int(x) for x in input().split()]
    twos = 0
    rest = 0
    for i in range(n):
        if ls[i] == 0 or ls[i] == 1:
            continue
        elif ls[i] == 2:
            twos += 1
        else:
            rest += 1
    ans = twos * rest + rest * (rest - 1) // 2
    print(ans)
