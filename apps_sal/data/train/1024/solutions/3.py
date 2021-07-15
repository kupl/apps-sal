# cook your dish here
sTot = 0
for _ in range(int(input())):
    s,n,k,r = map(int,input().split())
    if r == 1:
        sn = k*n
    else:
        sn = k*(r**n-1)/(r-1)
    if sn<=s:
        print("POSSIBLE",int(s-sn))
        sTot += s-sn
    else:
        print("IMPOSSIBLE",int(sn-s))
        sTot -= sn-s
if sTot >= 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
