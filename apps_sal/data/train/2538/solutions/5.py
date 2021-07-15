class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        groups = [0]
        
        for i in range(1, n+1, 1):
            sumDigi = self.sumOfDigits(i)
            if (sumDigi == len(groups)):
                groups.append(0)
            groups[sumDigi]+=1            
        #print(groups)
        
        
        
        maxGroup = 0
        maxCount = 0
        for grp in groups:
            if (grp > maxGroup):
                maxGroup = grp
                maxCount = 0
            if (grp == maxGroup):
                maxCount += 1
        #print(\"maxGroup=%d, maxCount=%d\" % (maxGroup, maxCount))
                
        return maxCount
        
        
        
    def sumOfDigits(self, n:int) -> int:
        sum = 0
        while (n>0):
            sum += n%10
            n //= 10
        return sum
