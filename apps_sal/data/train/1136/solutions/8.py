# cook your dish here
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    print(int((n + 1) / 2) * k)
