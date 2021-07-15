# cook your dish here
T=int(input())
for i in range(0,T):
    lst2=[]
    N=int(input())
    for j in range(0,N):
        lst=input()
        lst2.append(lst)
    print(int(N*(N+1)/2))
