class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        \"\"\"
        #O(n^2) working sol
        ans = [1 for i in range(len(rains))]
        d = collections.defaultdict(int)
        d[0]=0
        
        for i in range(len(rains)):
            d[rains[i]]+=1
            if rains[i]==0:
                #look for the nearest value that exists in the dict we got
                for x in range(i+1,len(rains)):
                    if rains[x] in d and not rains[x]==0:
                        #print(d,d[rains[x]],rains[x])
                        d[0]-=1
                        ans[i] = rains[x]
                        d[rains[x]]-=1
                        if d[rains[x]]==0: del d[rains[x]]
                        break
            else:
                #you gotta get out early of a bad pattern that cannot be salvaged
                if d[rains[i]]>1:
                    return []
                ans[i] = -1
        
        return ans
        \"\"\"
        
        ans = [1 for i in range(len(rains))]
        d = collections.defaultdict(int)
        d[0]=0
        #preprosess, find all  #:0#0#0...
        # as d grows, put corresponding value here in a heap
        # every time heap pops, we get the nearest value that exists in the dict we got
        p = {}
        x = collections.defaultdict(int)
        x[0] = 0
        for i in range(len(rains)):
            if rains[i] in p:
                #print(x[0],rains[i],x[rains[i]])
                if x[0]>=x[rains[i]]:
                    p[rains[i]] += [i]
            else:
                p[rains[i]] = []
            x[rains[i]]+=1
        p[0] = []
            
        #print(p)       
            
        s= set()
        h = []
        for i in range(len(rains)):

            d[rains[i]]+=1

            if rains[i]!=0 and rains[i] not in s:
                if rains[i] in p and p[rains[i]] != []:
                    for j in p[rains[i]]:
                        heappush(h,j)
                s.add(rains[i])
            #print(d,h)
             
            if rains[i]==0:
                #look for the nearest value that exists in the dict we got
                if h:
                    pop = heappop(h)
                    d[0]-=1
                    
                    ans[i] = rains[pop]
                    if rains[pop] not in d:
                        rains[pop] = 1
                    else:
                        d[rains[pop]]-=1
                    if d[rains[pop]]==0: del d[rains[pop]] 
            else:
                
                #you gotta get out early of a bad pattern that cannot be salvaged
                if d[rains[i]]>1:
                    return []
                #find the next equal closest value past a zero.
                ans[i] = -1
            #print(h,i,\"heap at end\")
        
        return ans
        
        
        
        
                
        
                
            
            
        
            
        
                        
                        
        
                
       
        
                
                
                
