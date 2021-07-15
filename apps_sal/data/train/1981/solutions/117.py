class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        '''
        Tricky part is finding the permutation that will result in maximum
        sum of the requests
        
        Looping through all permutations will likely TLE
        
        Setup nums in a way such that requests is maximized.
        
        Do it in greedy way + sort
        Have the max values be at the largest request interval
        
        How to deal with overlapping requests
        
        Largest number goes in index with most
        overlappings, second largest goes to index
        with second most overlappings etc.
        
          -
          - - -
        - - -
        0 1 2 3 4 5
        1 2 3 4 5 9
         
        requests
        [[0,2],[1,3],[1,1]]
        
        overlaps
        
        0 1 2 3 4 5
        1 3 2 1 0 0
        
        1 2 0 3 4 5
        3 2 1 1 0 0
        
        0 1 2 3 4 5
        4 9 5 3 2 1
        
        For each index calculate the number of request that overlap it
        Better to do this the other way around.
        
        This still TLEs
        
        O(nlogn)
        
        Your implementation is not actually O(nlogn) see
        comment in code
        '''
        if not nums or not requests: return 0
        
        overlaps = [(i, 0) for i in range(len(nums) + 1)]
        for start, end in requests:
            overlaps[start] = (overlaps[start][0], overlaps[start][1] + 1)
            overlaps[end + 1] = (overlaps[end + 1][0], overlaps[end + 1][1] - 1)
            
        for i in range(1, len(overlaps)):
            overlaps[i] = (overlaps[i][0] , overlaps[i][1] + overlaps[i - 1][1])
        
        overlaps.pop()
        overlaps.sort(key=lambda tup: tup[1], reverse=True)
        nums.sort()
        max_permutation = [0] * len(nums)
        for i, freq in overlaps:
            max_permutation[i] = nums[-1]
            nums.pop()
        
        prefix_sum = [max_permutation[0]]
        for i in range(1, len(max_permutation)):
            prefix_sum.append(prefix_sum[i - 1] + max_permutation[i])
        
        sum = 0
        for start, end in requests:
            right = prefix_sum[end]
            left = 0 if start == 0 else prefix_sum[start - 1]
            sum += right - left
        
        return sum % (10**9 + 7)

    
    def maxSumRangeQuery_1(self, nums: List[int], requests: List[List[int]]) -> int:
        '''
        Discuss Solution thats faster at detecting
        the number of requests that overlap an index.
        
        Key Idea have array t, loop
        through requests [[start, end] ...]
        
        Make t[start] += 1 to indicate
        every index after start is counted once
        for this request overlap
        Make t[end + 1] -= 1 to indicate
        every index after end + 1 is counted one less
        for this request overlap
        
        The prefix sum of array t tells us
        the number of requests that overlap
        an index
        
        requests
        [[0,2],[1,3],[1,1]]
        
          -
          - - -
        - - -
        0 1 2 3 4 5
        1 2 3 4 5 9
        
        t
        0  1  2  3  4  5  6
        1  2 -1 -1 -1
        
        t_prefix
        0  1  2  3  4  5  6
        1  3  2  1  0  0  0
        
        t.pop to remove index 6
        Sort both nums and t and
        use zip to line them up
        This matches most frequently
        overlapped index with biggest
        num.
        
        nums
        1 2 3 4 5 9
        t
        0 0 1 1 2 3
        
        Multiply because index i gets overlapped
        t[i] times so the nums value of mapping
        also gets mulitplied that number of times
        for the sum
        
        nums[i] * t[i]
        0 0 3 4 10 27
        
        sum of final = 44
        '''
        t = [0] * (len(nums) + 1)
        
        for start, end in requests:
            t[start] += 1
            t[end + 1] -= 1
            
        for i in range(1, len(nums)):
            t[i] += t[i - 1]
        
        nums.sort()
        t.pop() # Makes it so t matches length with nums
        t.sort()

        return sum(a*b for a, b in zip(nums, t)) % (10**9 + 7)
            
        
            

