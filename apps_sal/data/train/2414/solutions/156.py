class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # triplets_num = 0
        # for i in range(len(arr)-2):
        #     for j in range(i+1, len(arr)-1):
        #         if abs(arr[i]-arr[j]) <= a:
        #             for k in range(j+1, len(arr)):
        #                 if abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
        #                     triplets_num += 1
        # return triplets_num
        
        comb = combinations(list(range(len(arr))), 3)
        condition = lambda i, j, k: i < j and j < k and abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c
        return len([(i, j, k) for (i, j, k) in comb if condition(i, j, k)])
            

