n=int(input())
L=list(map(int,input().split()))
friends=int(input())
li=[]
for _ in range(friends):
    fB=L.pop(int(input())-1)
    li.append(fB)
for i in li:
    print(i)
