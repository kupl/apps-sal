class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # ans = -1
        # visited = []
        # for x in range(len(arr)):
        #     if arr[x] not in visited:
        #         visited.append(arr[x])
        #         if arr.count(arr[x]) == arr[x]:
        #             ans = max(ans,arr[x])
        #             print(ans)
        # return ans
        
        dict={}
        ans=-1
        for x in range(len(arr)):
            if arr[x] not in dict:
                dict[arr[x]] = 1
            else:
                dict[arr[x]] += 1
        for key,value in dict.items():
            if key == value:
                ans = max(ans,key)
        return ans
