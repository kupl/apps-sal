#bd = binary dict
#soen = sum of each number
class Solution:
    
    def longestAwesome(self, s: str) -> int:
        # generate list of existing binaries
        bd = {}
        bd[0] = -1 # remember when searching start from index -1
        #soen = [0 for i in range(10)]
        soen = 0
        
        for i,n in enumerate(s): # first loop
            #binary operation
            soen ^= 1<<int(n)
            bd[soen] = -1
        
            # update dictionary with the latest index that can form awesome string
            bd[soen] = i
            for j in range(10):
                soen_cpy = soen
                soen_cpy ^=1<<j
                if soen_cpy in bd:
                    bd[soen_cpy] = i 
        
        soen = 0
        max_ = bd[0]+1
        for i,n in enumerate(s):
            soen ^= 1<<int(n)
            cur_max = bd[soen] - i
            if cur_max>max_:
                max_ = cur_max
        return max_

