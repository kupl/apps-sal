r = int(input())
while r > 0:
    n, k, d = map(int, input().split())
    l = list(map(int, input().split()))[0:n]
    sum = 0
    for x in range(n):
        sum = sum + l[x]
    c = sum // k
    if (c >= d):
        print(d)
    else:
        print(c)
    r -= 1
"""""
5
1 5 31
4
1 10 3
23
2 5 7
20 36
2 5 10
19 2
3 3 300
1 1 1
"""""
