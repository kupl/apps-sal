# cook your dish here
try:
    t = int(input())
    for i in range(0, t):
        a, b = map(int, input().split())
        if(a > b):
            print(a, a + b)
        else:
            print(b, a + b)
except:
    pass
