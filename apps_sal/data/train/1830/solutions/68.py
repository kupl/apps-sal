class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        
        res=[]
        for rain in rains:
            if rain>0:
                res.append(-1)
            else:
                res.append(1)
        
        #full_lakes=[]
        full_lakes=defaultdict(list)
        
        #index of 0
        sunny_days=[]
        
        
        #remove leading and trailing zeros
        start=0
        end=len(rains)-1
        while rains[start]==0:
            start+=1
        while rains[end]==0:
            end-=1

        def binarySearch(sunny_days,prev_rain,curr):
            #print('binary seaarch: ',sunny_days,prev_rain,curr)
            if not sunny_days:
                return -1
            low=0
            high=len(sunny_days)
            while low<high:
                mid=(low+high)//2

                if sunny_days[mid]<=prev_rain:
                    low=mid+1
                else:
                    high=mid
            #print(low)
            if low>=len(sunny_days) or sunny_days[low]<=prev_rain or sunny_days[low]>=curr:
                return -1
            else:
                return low
                
        # a=[8]
        # b=9
        # c=10
        # print(binarySearch(a,b,c))

            
            
        
        for i in range(start,end+1):
            if rains[i]!=0:
                if rains[i] not in full_lakes or not full_lakes[rains[i]]:
                    full_lakes[rains[i]].append(i)
                else:
                    prev_rain=full_lakes[rains[i]][-1]

                    
                    #print(prev_rain,i,sunny_days)
                    #print('#####')
                    if not sunny_days:
                        return []
                    
                    idx=binarySearch(sunny_days,prev_rain,i)
                    #print(idx)
                    #print(sunny_days,prev_rain,i)
                    # for j in range(len(sunny_days)):
                    #     if prev_rain<sunny_days[j]<i:
                    #         idx=sunny_days[j]
                    #         break
                    if idx==-1:
                        return []
                    else:
                        
                        res[sunny_days[idx]]=rains[i]
                        full_lakes[rains[i]].pop()
                        full_lakes[rains[i]].append(i)
                        sunny_days.pop(idx)
                        
            else:
                sunny_days.append(i)
        return res
        
                    
                        
        

