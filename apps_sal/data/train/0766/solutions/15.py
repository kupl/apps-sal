# cook your dish here
# cook your dish here
for i in range(int(input())):
    N=int(input())
    Arr=list(map(int,input().split()))
    Arr.sort()
    print(Arr[-1]*Arr[-2],Arr[0]*Arr[1])

