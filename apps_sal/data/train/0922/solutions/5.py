# cook your dish here
T=int(input())
for t in range(T):
    z=input()
    N,M=z.split()
    N,M=int(N),int(M)
    z=input()
    first=z.split()
    second=input().split()
    first=[int(i) for i in first]
    second=[int(i) for i in second]
    set_1=set()
    set_2=set()
    for i in first:
        if i not in set_1:
            set_1.add(i)
    for i in second:
        if i not in set_2:
            set_2.add(i)
    output=[]
    for i in first:
        if i not in set_2:
            output.append(i)
    for i in second:
        if i not in set_1:
            output.append(i)
    for i in output:
        print(i,end=" ")
