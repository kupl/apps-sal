class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # |arr[i] - arr[j]| <= a
        # |arr[j] - arr[k]| <= b
        # |arr[i] - arr[k]| <= c
        triplets=0
        for i in range(len(arr)-2):
            for j in range(i+1,len(arr)-1):
                for k in range(j+1,len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        triplets+=1
                        # print((arr[i],arr[j],arr[k]))
        return triplets
