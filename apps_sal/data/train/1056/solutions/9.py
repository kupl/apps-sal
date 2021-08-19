# cook your dish here
try:
    t = int(input())
    for i in range(0, t):
        a, b, c = map(int, input().split())
        if(a + b + c == 180):
            print("YES")
        else:
            print("NO")
except:
    pass
