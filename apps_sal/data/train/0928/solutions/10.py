x=[]
for i in range(1,31624):
    if (i*i)%3!=0:
        x.append(i*i)

m= len(x)
for i in range(int(input())):
    n= int(input())
    if n<x[0]:
        print(0)
    elif n>x[-1]:
        print(m)
    else:
        for j in range(m):
            if x[j]>n:
                break
        print(j)



