S = input().split()
N=len(S)
sml=len(S[0])
val=S[0]
for i in S:
    if len(i)<sml:
        sml=len(i)
        val=i
print(val,end=' ')
i=0
while i<N:
    print(S[i],val,end=' ')
    i+=1
