t = int(input())
for i in range(t):
    h, m = list(map(int, input().split()))
    if(h >= m):
        print("Yes")
    else:
        print("No")
