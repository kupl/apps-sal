k = int(input())
for j in range(k):
    a, b, c = list(map(int, input().split()))
    l = []
    l = list(map(int, input().split()))
    s = sum(l)
    if(s < b):
        print("0")
    else:
        d = int(s / b)
        if(d < c):
            print(d)
        else:
            print(c)
