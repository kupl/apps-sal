from sys import stdin, stdout

n,k = list(map(int,stdin.readline().rstrip().split()))

print(2+(n-2)//k+(n-3)//k)

connectionsList = []
# Leaf node is 1. Make this node have connections to k children
for i in range(k):
    connectionsList.append((str(1),str(i+2)))


for i in range(k+2,n+1):
    connectionsList.append((str(i-k),str(i)))

for conn in connectionsList:
    print(' '.join(conn))

