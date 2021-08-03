from sys import*
input = stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    l = [int(x) for x in input().split()]
    mp = {}
    for items in l:
        try:
            mp[items] += 1
        except:
            mp[items] = 1
    l = list(set(l))
    l.sort()
    for items in l:
        if mp[items] > k:
            print(items, end=" ")
    print()
