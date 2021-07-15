class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = []
        for i in range(len(arr)):
            for j in range(1,len(arr)):
                for k in range(2,len(arr)):
                    if i<j<k:
                        if (abs(arr[i]-arr[j])<=a ) and (abs(arr[j] - arr[k]) <=b) and (abs(arr[i]-arr[k]) <=c):
                            res.append((arr[i],arr[j],arr[k]))
        return len(res)


