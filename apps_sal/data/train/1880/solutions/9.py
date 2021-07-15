class Solution:
    # 1,2,3,4,2,3,4,2,3,4,2  N = 11
    # groupSize
    # 0 1 2 3 4 5 6 7 8 9 0
    # x = 4 pos = 1
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        iterations = {}
        x = 0
        lastGroup = False
        while x < N:
            iteration = tuple(cells)
            if not lastGroup:
                if iteration in iterations:
                    print ('first',x, iteration)
                    lastGroup = True
                    pos = iterations[iteration]
                    #we found a cycle
                    groupSize = x-pos
                    print ('groupSize',groupSize )
                    groups = (N-pos)//groupSize
                    x = pos + groups*groupSize 
                    if x == N:
                        break
                    print (\"**\",x)
                else:
                    print(x, iteration)
                    iterations[iteration] = x
            #curr = cells.copy()
            prev = cells[0]
            if x ==0:
                cells[0]=0
            for i in range (1,len(cells)-1):
                if prev == cells[i+1]:
                    prev = cells[i]
                    cells[i] =1
                else:
                    prev = cells[i]
                    cells[i]=0
                    
            if x == 0:
                cells[-1]=0
            # increment x
            x+= 1
            #curr = cells.copy()
        return cells
                    
        
