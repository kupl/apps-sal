class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        \"\"\"
        Assume:
        1. list, list -> int
        2. only find sum, permutation is not unique
        3. nums is not sorted
        
        
        Algorithm:
        sort nums
        
        in requests, count number of coverage for each index. 
        counts = [c0, c1]
        put (c0, 0), (c1, 1) into maxHeap
        popout maxHeap, each index gets the assigned element from largest to smallest to form new nums
        
        calculate sum of requests in new nums
        
        Complexity:
        time: max(O(nlogn), O(mn))
        space: O(n)
        
        Follow up:
        1. use LinkedHashMap
        2. 
        
        \"\"\"
        if not nums:
            return -1 # rise IllegalInputArgumentException
        
        MOD = 10 ** 9 + 7
        result, n, m = 0, len(nums), len(requests)
        counts = [0 for _ in range(n)]
        max_heap = []
        
        # O(m*n)
        #for i in range(m):
        #    for j in range(requests[i][0], requests[i][1] + 1):
        #        counts[j] += 1
                
        # O(max(m, n)): use sweep line
        records = []
        for i in range(m):
            records.append([requests[i][0], 1])
            records.append([requests[i][1]+1, -1])
        for index, delta in sorted(records):
            if index < n:
                counts[index] += delta
        for i in range(n):
            if i != 0:
                counts[i] = counts[i] + counts[i-1]
        
        for i in range(n):
            heapq.heappush(max_heap, (-counts[i], i))
        
        # O(nlogn)
        nums.sort()
        new_nums, cur_max = [0 for _ in range(n)], n - 1
        while max_heap and cur_max >= 0:
            cur = heapq.heappop(max_heap)
            new_nums[cur[1]] = nums[cur_max]
            cur_max -= 1
        
        prefixsum = [0 for _ in range(n)]
        for i in range(n):
            if i == 0:
                prefixsum[i] = new_nums[i]
            else:
                prefixsum[i] = prefixsum[i-1] + new_nums[i]
        # print(f'counts:{counts}, new_nums:{new_nums}')
        for i in range(m):
            result += prefixsum[requests[i][1]] - prefixsum[requests[i][0]] + new_nums[requests[i][0]]
        return result % MOD
        
        
        
        
