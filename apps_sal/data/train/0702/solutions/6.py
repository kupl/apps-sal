t = int(input())
for _ in range(t):
    m, c, h = map(int, input().split())
    if((h - c) % 3 == 0):
        if((h - c) // 3 <= m):
            print("No")
        else:
            print("Yes")
    else:
        print("Yes")
