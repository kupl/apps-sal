# cook your dish here
# cook your dish here
try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = 1
        a = [int(x) for x in input().split()]
        for item in a:
            p = p * item
        if p % 2 == 0:
            print("NO")
        else:
            print("YES")

except:
    pass
