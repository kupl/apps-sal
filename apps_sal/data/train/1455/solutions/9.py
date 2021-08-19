import sys
n = eval(input())
lists = list(map(int, sys.stdin.readline().split()))
for __ in range(eval(input())):
    (l, r) = [x - 1 for x in list(map(int, sys.stdin.readline().split()))]
    k = [i for i in sorted(lists[l:r + 1])]
    ans = 0
    for i in range(1, len(k)):
        ans += (k[i - 1] - k[i]) ** 2
    print(ans)
