# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    str = list(map(int, input().split()))
    t = int(input())
    x = str[t - 1]
    str.sort()
    print(str.index(x) + 1)
