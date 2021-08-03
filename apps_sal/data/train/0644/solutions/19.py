t = int(input())
for _ in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    p = sum(ls)
    if p % n == 0:
        print("Yes")
    else:
        print("No")
