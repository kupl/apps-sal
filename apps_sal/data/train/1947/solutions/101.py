class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        
        def counter(c):
            listed = [0]*26
            for i in c:
                x=ord(i)-97
                listed[x]+=1
                
            return listed
        
        
        
        blist = [0]*26
        for b in B:
            temp_list = counter(b)
            for i in range(0,26):
                blist[i]= max(blist[i],temp_list[i])
        listed=blist
        l=[]
        
        for a in A:
            temp_list = counter(a)
            universal = True
            for i in range(0,26):
                if listed[i] > temp_list[i]:
                    universal = False
                    
            if universal:
                l.append(a)
        
        
        
        return l
    

