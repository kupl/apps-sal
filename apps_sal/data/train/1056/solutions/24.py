t = int(input())
i = 0
while i < t:
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if a + b + c == 180:
        print("YES")
    else:
        print("NO")
    i += 1
