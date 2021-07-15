class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        # i < j < k
        # |arr[i] - arr[j]| <= a
        # |arr[j] - arr[k]| <= b
        # |arr[i] - arr[k]| <= c
        la = len(arr)
        cnt = 0
        for i in range(la-2):
            for j in range(i+1,la-1):
                if abs(arr[i] - arr[j])<=a:
                    for k in range(j+1,la):
                        if abs(arr[j] - arr[k])<=b:
                            if abs(arr[i] - arr[k])<=c:
                                cnt +=1
        return cnt

