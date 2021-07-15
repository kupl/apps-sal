# cook your dish here
t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    if n % 2 != 0:
        print(((n+1)//2) * k)
    else:
        print((n//2)*k)
