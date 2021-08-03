from collections import Counter
for _ in range(int(input())):
    n = int(input())
    cnt = Counter()
    l = list(map(int, input().split()))
    for i in l:
        cnt[i] += 1
    if len(cnt.keys()) == 8:
        print(min(set(cnt.values())))
    else:
        print(0)
