class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        a = set()
        out=0
        for i in range(len(arr1)):
            for j in arr2:
                if abs(arr1[i]-j)<=d:
                    out+=1
                    if i not in a:
                        a.add(i)

        return len(arr1)-len(a)
