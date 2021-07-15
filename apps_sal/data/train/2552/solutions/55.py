class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        from scipy import stats
        x=stats.mode(arr)
        y=int(x[1])*100/len(arr)
        if y>25:
            return int(x[0])
            
s=Solution()
print(s.findSpecialInteger)
