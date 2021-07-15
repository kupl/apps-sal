class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        cnt=0
        for a in arr1:
            mark=0
            for b in arr2:
                if abs(a-b) <=d:
                    mark=1
            cnt+=1 if mark==0 else 0
        return cnt

