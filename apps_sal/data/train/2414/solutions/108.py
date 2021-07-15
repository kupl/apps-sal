class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count_ = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    diff1 = abs(arr[i] - arr[j])
                    diff2 = abs(arr[j] - arr[k])
                    diff3 = abs(arr[i] - arr[k])
                    if (diff1<=a) and (diff2<=b) and (diff3<=c):
                        count_ +=1
                        
        return count_
