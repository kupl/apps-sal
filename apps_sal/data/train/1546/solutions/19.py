tc = int((input()))
for _ in range(tc):
    n = list(map(int, input().split()))
    n.sort(reverse=True)
    if (n[0] <= 0 or n[1] <= 0 or n[2] <= 0):
        print("NO")
    elif n[0] * n[0] == ((n[1] * n[1]) + (n[2] * n[2])):
        print("YES")
    else:
        print("NO")
