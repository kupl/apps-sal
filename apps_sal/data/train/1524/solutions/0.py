ways = x = 0
val = 10**9
remi = ((10**9) + 7)
t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    if t <= 100 and n >= 1 and k <= val:
        x = (k - 1)**(n - 1)
        ways = k * x
        ways = ways % remi
        print(ways)
        x = ways = 0
    else:
        break
