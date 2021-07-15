teams=int(input())
strength=list(map(int, input().split()))
rev=0
for i in range(0,teams):
    for j in range(i+1,teams):
        if(strength[i]>strength[j]):
            rev+=strength[i]-strength[j]
            
        else:
            rev+=strength[j]-strength[i]
            
print(rev)

