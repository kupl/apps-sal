# cook your dish here
val = int(input())
for i in range(val):
    n, p = input().split()
    n = int(n)
    p = int(p)
    di = int(0)
    ca = int(0)
    q = list(map(int, input().split()))
    for j in range(len(q)):
        d = p / 10
        c = p / 2
        if(q[j] <= d):
            di = di + 1
        elif(c <= q[j]):
            ca = ca + 1
    if(ca == 1 and di == 2):
        print("yes")
    else:
        print("no")
