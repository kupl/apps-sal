n = int(input())

for i in range(n):
    a, b, c = map(int, input().split())

    a2 = int(pow(a, 2))
    b2 = int(pow(b, 2))
    c2 = int(pow(c, 2))

    if(a == 0 or b == 0 or c == 0):
        print("NO")
        continue

    if(a2 + b2 == c2):
        print("YES")
    elif(c2 + b2 == a2):
        print("YES")
    elif(a2 + c2 == b2):
        print("YES")
    else:
        print("NO")
