t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if(n % (k * k) == 0):
        print("NO")
    else:
        print("YES")
    t -= 1
