class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    if self.isGood(arr[i], arr[j], a) and self.isGood(arr[j], arr[k],b) and self.isGood(arr[i], arr[k], c):
                        count+=1
        return count
        
    def isGood(self, x, y, a):
        return abs(x - y) <= a

