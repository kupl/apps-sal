class Solution:
    def removeCoveredIntervals(self, arr: List[List[int]]) -> int:
        arr.sort(reverse=True)
        ans=0
        n=len(arr)
        take=[1]*n
        for i in range(n-1):
            for j in range(i+1,n):
                if arr[i][0]>=arr[j][0] and arr[i][1]<=arr[j][1]:
                    take[i]=0
                    break
        # print(arr)
        # print(take)
        for i in range(n-1,-1,-1):
            for j in range(i-1,-1,-1):
                if arr[i][0]>=arr[j][0] and arr[i][1]<=arr[j][1]:
                    take[i]=0
                    break
        # print(arr)
        # print(take)
        return take.count(1)
