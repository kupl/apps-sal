n=int(input())
nlist=[int(x) for x in input().split()]
xor=[[0]*2**21 for xor in range(2)]
x=counter=0
xor[1][0]=1
for i in range(n):
    x^=nlist[i]
    counter+=xor[i%2][x]
    xor[i%2][x]+=1
print(counter)

