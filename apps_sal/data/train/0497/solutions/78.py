class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
        diff from max intervals. 

        either take or dont take a certain interval.

        then do max
        Do top down then bottom up. 

        Greedy -> earliest finishing time. 

        Sort by finishing time. 
        Choose it or dont. 
        Always choose it if it doesnt interfere with the next one. 

        you can binary search the end time in the start times to find the next available start times you can take. 


        So DP[i] -> max profit after processing interval i. 

        '''
        N = len(startTime)

        # sort by start times

        res = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        # print(\"res\", res)

        # unzip it now!
        unzipped_res = list(zip(*res))

        startTime = unzipped_res[0]
        endTime = unzipped_res[1]
        profit = unzipped_res[2]

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

            for j in range(i + 1, N):

                if startTime[j] >= end:
                    nextI = j
                    break

            prof = profit[i]

            # take it
            taken = solve(nextI) + profit[i]

            # dont take:
            notTaken = solve(i + 1)
            # print(\"nextI, TAKEN AND NOT TAKEN ARE\", i,nextI, taken, notTaken)
            return max(taken, notTaken)

        amt = solve(0)
        return amt
