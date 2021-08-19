# cook your dish here
def invper(ar):
    ar1 = [0] * (len(ar))
    for i in range(1, len(ar)):
        ar1[ar[i]] = i
    return ar1


t = int(input())
while(t != 0):
    ar = list(map(int, input().split()))
    ar.insert(0, 0)
    ar1 = invper(ar)
    if(ar == ar1):
        print("ambiguous")
    else:
        print("not ambiguous")
    t = int(input())
