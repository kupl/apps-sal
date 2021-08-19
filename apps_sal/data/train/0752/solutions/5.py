# cook your dish here
n, q = map(int, input().split())
x = {}
for j in range(n):
    a, b = map(str, input().split())
    x[a] = b
for i in range(q):
    h = input().strip()
    if("." in h):
        c = h.split(".")[-1]
        if(c in x):
            print(x[c])
        else:
            print("unknown")
    else:
        print("unknown")
