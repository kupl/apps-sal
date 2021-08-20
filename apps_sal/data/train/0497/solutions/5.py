class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        diff from max intervals. 
        Sort by Start Time (dont do the greedy sort by earliest finish time)
        Choose it or dont. 
        Always choose it if it doesnt interfere with the next one. 
        you can binary search the end time in the start times to find the next available start times you can take. 

        Have 3 solutions.
        """
        res = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        unzipped_res = list(zip(*res))
        startTime = unzipped_res[0]
        endTime = unzipped_res[1]
        profit = unzipped_res[2]
        return self.backwardDP(startTime, endTime, profit)

    def topDown(self, startTime, endTime, profit):
        N = len(startTime)
        '\n        Thought I would need to do the other params like \n        endTime or maxProfit but dont have to because \n        parent call does not have to communicate to child recursive calls\n        to help child recursive calls to achieve max. Since we\n        dont need parent-child communication, we can get away with \n        passing very little info to child through its function params.\n        '

        @lru_cache(None)
        def solve(i):
            if i == N:
                return 0
            start = startTime[i]
            end = endTime[i]
            nextI = N
            for j in range(i + 1, N):
                if startTime[j] >= end:
                    nextI = j
                    break
            prof = profit[i]
            taken = solve(nextI) + profit[i]
            notTaken = solve(i + 1)
            return max(taken, notTaken)
        amt = solve(0)
        return amt

    def backwardDP(self, startTime, endTime, profit):
        from bisect import bisect_left
        '\n        \n        So the states I need is \n        max profit achieved at each index. \n        then we binary search to the right an index we can use to include\n        in our max profit!\n        \n        and process backwards like that!\n        \n        OPT[i] = max(Take, DontTake)\n                    OPT[i`] + profit[i], OPT[i-1]\n                    \n        \n        '
        N = len(startTime)
        OPT = [0 for i in range(N + 1)]
        for i in range(N - 1, -1, -1):
            start = startTime[i]
            end = endTime[i]
            prof = profit[i]
            freeK = N
            '\n            Linear search that leads to O(N^2)\n            for k in range(i+1, N):\n                if end <= startTime[k]:\n                    freeK = k\n                    break    \n            '
            freeK = bisect_left(startTime, end)
            take = profit[i] + OPT[freeK]
            dontTake = OPT[i + 1]
            OPT[i] = max(take, dontTake)
        return OPT[0]

    def forwardDP(self, startTime, endTime, profit):
        """
        Ok look at idx 0
            -> Is there a way to do it NlogN?
            -> find all intervals to right that dont intersect with us!
            -> add it in. 

        Is this the brute force solution or what does the brute force 
        solution look like?

        Actaully this one is very difficult
        """
        N = len(startTime)
        OPT = [profit[i] for i in range(N)]
        for i in range(N):
            prof = profit[i]
            end = endTime[i]
            x = bisect_left(startTime, end)
            for k in range(x, N):
                OPT[k] += prof
        return OPT[-1]
