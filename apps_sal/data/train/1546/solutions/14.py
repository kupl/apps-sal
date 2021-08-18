for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if(a == 0 or b == 0 or c == 0):
        print("NO")
        continue
    if(a * a + b * b == c * c):
        print("YES")
    elif(a * a + c * c == b * b):
        print("YES")
    elif(b * b + c * c == a * a):
        print("YES")
    else:
        print("NO")
