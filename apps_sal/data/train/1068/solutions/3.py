t = int(input())
for i in range(0, t):
    (a, b) = list(map(int, input().split()))
    if(a % 2 == 0 or b % 2 == 0):
        print("YES")
    else:
        print("NO")
