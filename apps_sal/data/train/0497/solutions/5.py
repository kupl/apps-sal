class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
        diff from max intervals. 
        Sort by Start Time (dont do the greedy sort by earliest finish time)
        Choose it or dont. 
        Always choose it if it doesnt interfere with the next one. 
        you can binary search the end time in the start times to find the next available start times you can take. 
        
        Have 3 solutions.
        '''
       
        # sort by start times
        res = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        # unzip it now!
        unzipped_res = list(zip(*res))
        startTime = unzipped_res[0]
        endTime = unzipped_res[1]
        profit = unzipped_res[2]
        
        #return self.topDown(startTime, endTime, profit)
        return self.backwardDP(startTime, endTime, profit)
        # return self.forwardDP(startTime, endTime, profit)
    
    # TOP DOWN COMPLETED.
    def topDown(self, startTime, endTime, profit):
        N = len(startTime)
        
        # Only memoizing one param
        '''
        Thought I would need to do the other params like 
        endTime or maxProfit but dont have to because 
        parent call does not have to communicate to child recursive calls
        to help child recursive calls to achieve max. Since we
        dont need parent-child communication, we can get away with 
        passing very little info to child through its function params.
        '''
        @lru_cache(None)
        def solve(i):
            
            if i == N:
                return 0
            
            # either take or dont
            start = startTime[i]
            end = endTime[i]
            
            # you can skip to the index that has a start time ahead of 
            # end time -> so that you dont have to 
            # pass along endtime in memtable? 
            
            nextI = N
            
            # CAN USE BINARY SEARCH HERE!
            for j in range(i+1, N):
                if startTime[j] >= end:
                    nextI = j
                    break
                    
            prof = profit[i]
            
            # take it
            taken = solve(nextI) + profit[i]
            
            # dont take:
            notTaken = solve(i+1)
            # print(\"nextI, TAKEN AND NOT TAKEN ARE\", i,nextI, taken, notTaken)
            return max(taken, notTaken)
        
        amt = solve(0)
        return amt
            
    def backwardDP(self, startTime, endTime, profit):      
        from bisect import bisect_left
        
        # Bottom Up.
        '''
        
        So the states I need is 
        max profit achieved at each index. 
        then we binary search to the right an index we can use to include
        in our max profit!
        
        and process backwards like that!
        
        OPT[i] = max(Take, DontTake)
                    OPT[i`] + profit[i], OPT[i-1]
                    
        
        '''
        N = len(startTime)
        OPT = [0 for i in range(N+1)]
        
        for i in range(N-1, -1, -1):
            
            start = startTime[i]
            end = endTime[i]
            prof = profit[i]
            
            # Take operation
            # find the end index!
            
            # endI = bisect_left(end, startTime)
            # if endI < 
            freeK = N
            '''
            Linear search that leads to O(N^2)
            for k in range(i+1, N):
                if end <= startTime[k]:
                    freeK = k
                    break    
            '''
            # Has to be bisect_left not bisect_right!
            freeK = bisect_left(startTime, end)
            take = profit[i] + OPT[freeK]
            dontTake = OPT[i+1]
            OPT[i] = max(take, dontTake)
        return OPT[0]
    
    # COULD NOT DO FORWARD VERY HARD!
    def forwardDP(self, startTime, endTime, profit):
        '''
        Ok look at idx 0
            -> Is there a way to do it NlogN?
            -> find all intervals to right that dont intersect with us!
            -> add it in. 
            
        Is this the brute force solution or what does the brute force 
        solution look like?

        Actaully this one is very difficult
        '''
        N = len(startTime)
        OPT = [profit[i] for i in range(N)]
        
        for i in range(N):
            # find all intervals ahead of us! 
            # and add us in.
            
            prof = profit[i]
            end = endTime[i]
            
            x = bisect_left(startTime, end)
            for k in range(x, N):
                OPT[k] += prof
        
        return OPT[-1]
    
                        
            
            
            
            
        
            
            
        
        
         
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
            
            
        

