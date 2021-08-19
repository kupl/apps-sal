import sys
input = sys.stdin.readline
t = int(input())
for you in range(t):
    n = int(input())
    l = input().split()
    li = [int(i) for i in l]
    z = []
    for i in range(n):
        z.append(li[i])
    maxpref = [0 for i in range(n)]
    maxa = 0
    for i in range(n):
        maxa += z[i]
        maxpref[i] = maxa
    curr = 0
    count = 0
    while(curr < n - 1):
        curr += maxpref[curr]
        count += 1
        # print(curr)
    print(count)
