class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        for i in range(1,len(arr)):
            for j in range(len(arr[0])):
                above = []
                for k in range(len(arr[0])):
                    if k!=j:
                        heapq.heappush(above, arr[i-1][k])
                        #above.add()
                #print(above)
                #print(above)
                arr[i][j] = arr[i][j] + above[0]
        return min(arr[-1])
