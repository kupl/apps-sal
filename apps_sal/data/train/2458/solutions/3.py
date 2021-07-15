class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count1 = 0
        count2 = 0
        counter = 0
        for i in s:
            if i == 'R':
                
                count1 +=1
            else:
                
                count2 +=1
            if count1 == count2:
                
                counter +=1
        return counter
