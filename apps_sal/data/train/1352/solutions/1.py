from collections import Counter
n = int(input())
for c in range(n):
    t = int(input())
    s = list(map(int, input().strip().split()))
    count = dict(Counter(s))
    for k in sorted(count.keys()):
        answer = str(k) + ': ' + str(count[k])
        print(answer)
