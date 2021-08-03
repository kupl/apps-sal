'''
n=1
10

1
--------
n=3
8 3 6

2
--------
n=5
4 5 1 2 3

2
'''

t = int(input())
for i in range(t):
    n = int(input())
    l1 = list(map(int, input().split()))
    curr = l1[0]
    ans = 0
    for j in range(n):
        if(l1[j] <= curr):
            ans += 1
            curr = l1[j]
    print(ans)
