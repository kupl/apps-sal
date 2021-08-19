# cook your dish here
try:
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        l = list(map(int, input().split()))
        x1 = max(l)
        x2 = min(l)

        if((x1 - x2) < b):
            print("YES")
        else:
            print("NO")

except:
    pass
