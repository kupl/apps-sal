import sys
#q=1
q=int(input())
for i in range(q):
    #n,m=[int(j) for j in sys.stdin.readline().split()]
    n=int(sys.stdin.readline())
    a=[int(j) for j in sys.stdin.readline().split()]
    a=a[::-1]
    swap=0
    t=n
    for i in range(n-1):
        if swap==0:
            if a[i]>a[i+1]:
                swap=1
        elif swap==1:
            if a[i]<a[i+1]:
                swap=2
                t=i+1
                break
    print(n-t)

