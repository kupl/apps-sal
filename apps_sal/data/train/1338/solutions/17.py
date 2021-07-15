l=list(map(float,input().split()))
for x in range(1,len(l),2):
    print('%.2f'%(l[x]*(10**l[x+1])))

