t = int(input())
for _ in range(t):
    x, y, K, N = map(int, input().split())
    if abs(x - y) % 2 != 0:
        print("No")
    else:
        if abs(x - y) % K == 0 and (abs(x - y) // K) % 2 == 0:
            print("Yes")
        else:
            print("No")
