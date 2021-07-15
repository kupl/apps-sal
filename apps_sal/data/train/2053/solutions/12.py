l = input().split(" ")
n = int(l[0])
m = int(l[1])
B = input().split(" ")
B = [int(x) for x in B]
J = input().split(" ")
J = [int(x) for x in J]

J.sort()
B.sort()

if J[0] < B[-1]:
    print(-1)
    return
    
k=n-1
sm= sum(B)
l= (sm-B[-1])*m
s=l
for i in J:
    s+=i

if B[-1] != J[0] :
    s=s+B[-1]-B[-2]
print(s)
