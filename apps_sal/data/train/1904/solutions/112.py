import random

class Solution:
    def kClosest(self, nums: List[List[int]], k: int) -> List[List[int]]:
        dist =[]
        for i in range(len(nums)):
            dist.append(nums[i][0] **2 + nums[i][1] **2)
        #Create a hMap
        hMap={}
        for i in range(len(dist)):
            hMap[i] = dist[i]
            
        unique_ids = list(hMap.keys())
        
        def helper(unique_ids,k,start,end):
            if start >= end:
                return
            pivot_idx = random.randint(start,end)
            
            unique_ids[start],unique_ids[pivot_idx] = unique_ids[pivot_idx], unique_ids[start]
            
            pivot = hMap[unique_ids[start]]
            
            smaller = start
            
            for bigger in range(start+1, end+1):
                if hMap[unique_ids[bigger]] <= pivot:
                    smaller +=1
                    unique_ids[smaller], unique_ids[bigger] = unique_ids[bigger],unique_ids[smaller]
                    
            unique_ids[start], unique_ids[smaller] = unique_ids[smaller],unique_ids[start]
            
            if k == smaller:
                return 
            elif k < smaller:
                helper(unique_ids,k,start,smaller-1)
            else:
                helper(unique_ids,k,smaller+1,end)
                
                
        
        helper(unique_ids,k,0,len(unique_ids)-1)
        return [nums[i] for i in unique_ids[:k]]

