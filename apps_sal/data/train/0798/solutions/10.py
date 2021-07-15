import numpy as np

n,mC = [int(i) for i in input().split()]
arr = np.array([[int(i) for i in input().split()] for j in range(n)] )
charms = [[int(i) for i in input().split()] for j in range(mC)]

block = 1001
safeArr = np.full((n,n),block)
inBounds = lambda ind: 0<=ind<n

for charm in charms:
    x,y,stg = charm
    x-=1
    y-=1
    
    maxWidth = stg*2+1

    seqX = []
    seqY = []
    ct = x-stg
    for i in range(maxWidth):
        l = stg-abs(stg-i)
        seqX.extend([ct]*(l*2+1))
        seqY.extend(list(range(y-l,y+l+1)))
        ct+=1
    
    safeCoords = np.array(list(filter(lambda x: inBounds(x[0]) and inBounds(x[1]), zip(seqX,seqY) )))
    finalCoords = (safeCoords[:,0],safeCoords[:,1])
    safeArr[finalCoords] = arr[finalCoords] # acceptable places

if (safeArr[0,0]==block) or (safeArr[-1,-1]==block):
    print('NO')
else:
    prevRow = safeArr[0].copy()
    for j in range(1,n):
        left = prevRow[j-1]
        if prevRow[j] != block:
            if left == block:
                prevRow[j] = block
            else:
                prevRow[j] += left
    
    for i in range(1,n):
        thisRow = safeArr[i].copy()
        if thisRow[0]!=block:
            if prevRow[0] == block:
                thisRow[0] = block
            else:
                thisRow[0] += prevRow[0]
                
        for j in range(1,n):
            up = prevRow[j]
            left = thisRow[j-1]           
            if thisRow[j] != block:
                if up == block:
                    if left == block:
                        thisRow[j] = block
                    else:
                        thisRow[j] += left
                elif left == block:
                    thisRow[j] += up
                else:
                    thisRow[j] += max(up, left)                
            
        prevRow = thisRow[:]
    final = prevRow[-1]
    if final == block:
        print('NO')
    else:
        print('YES')
        print(final)

