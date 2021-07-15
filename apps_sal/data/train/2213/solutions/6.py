def iA():
    n=[int(x) for x in input().split()]
    return n
def iI():
    n=int(input())
    return n
def iS():
    n=input()
    return n
def iAA(numArrs):
    n=[]
    for i in range(numArrs):
        m=iA()
        n.append(m)
    return n
def pA(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

for i in range(iI()):
    r=iA()
    t=r[0]^r[1]
    if r[2]%3==0:
        print(r[0])
    elif r[2]%3==1:
        print(r[1])
    else:
        print(r[0]^r[1])
