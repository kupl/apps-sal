e=[]
for i in range(10001):
    e.append(i*i)
for i in range(1,10001):
    e[i]+=e[i-1]
for _ in range(int(input())):
    n=int(input())
    print(e[n-1])

