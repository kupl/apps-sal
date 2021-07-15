class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
        Refer to Eva Tardos's 'Algorithm Design' - 6.1 Weighted Interval Scheduling
        
        First post in the discuss section explains the same approach
        
        Steps
        ------
        1. Sort and order jobs by the end time - O(n logn)
        
        2. Build a most_recent array with most_recent[j] being the index of the most recent disjoint job - O(n logn)
           ** use binary search to build this array ** 
           
        3. Calculate profit for each position using the relation - O(n)
           ** dp_profits[j] = max(profits[j] + dp_profits[previous[j]], dp_profits[j-1]) **
        '''
        
        # zip and order jobs by end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        
        '''
        for each job in jobs find the most recent disjoint
        this is nothing but finding the index of the floor of each start time in the sorted end times
        i.e. for each start time, finding the index of greatest end time less than or equal to start time
        
        if the floor is not present the value returned would be -1
        '''
        def binary_search(val: int):
            '''
            Try doing a dry run with test cases before implementing
            
            Always choose one test value in the left of mid, one in the right and one for each boundar condition.
            Refer to vscode playground floor.py
            '''
            nonlocal jobs
            
            # boundary conditions - note job = (start_time, end_time, profit)
            if val < jobs[0][1]:
                return -1
            if val >= jobs[-1][1]:
                return len(jobs) - 1
            
            start, end = 0, len(jobs) - 1
            
            while start < end - 1:
                mid = start + (end - start) // 2
                
                if jobs[mid][1] < val:
                    start = mid
                elif jobs[mid][1] > val:
                    end = mid -1
                else:
                    return mid
            
            return end if jobs[end][1] <= val else start
        
        most_recent = [0] * len(jobs)
        
        for i, job in enumerate(jobs):
            most_recent[i] = binary_search(job[0])
        
        '''
        Calculate profit for each job using recurrence relation and return the last value.
        
        
        '''
        dp_profits = [0] * len(jobs)
        for i, job in enumerate(jobs):
            most_recents_profit = 0 if most_recent[i] == -1 else dp_profits[most_recent[i]]
            prev_profit = 0 if i == 0 else dp_profits[i-1]
            
            dp_profits[i] = max(job[2] + most_recents_profit, prev_profit)
        
        return dp_profits[-1]
