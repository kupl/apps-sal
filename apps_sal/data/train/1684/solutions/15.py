t=int(input())
n=[]
for i in range(t):
    a=int(input())
    n.append(a)
for i in range(t):
    for j in range(n[i]):
        print(j+1,end=' ')
    print()

