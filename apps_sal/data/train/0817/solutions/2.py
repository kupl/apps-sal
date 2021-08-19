# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = 0
    for i in range(0, len(a)):
        x = x ^ a[i]
    print(x)
