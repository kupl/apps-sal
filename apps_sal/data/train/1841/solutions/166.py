class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        ls = len(arr)
        arr.sort()
        median = arr[(ls - 1) // 2]
        print(median)

        res = []
        i = 0
        for num in arr:
            if i == k:
                heapq.heappush(res, (abs(num - median), num))
                heapq.heappop(res)
            else:
                heapq.heappush(res, (abs(num - median), num))
                i += 1
        return [x[1] for x in res]
