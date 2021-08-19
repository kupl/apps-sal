# cook your dish here
t = int(input(""))
for i in range(t):
    x, r, a, b = map(int, input().split())
    win = max(a, b)
    rel = abs(a - b)
    d = (rel * x) / win
    if(d == int(d)):
        print(int(d - 1))
    else:
        print(int(d))
