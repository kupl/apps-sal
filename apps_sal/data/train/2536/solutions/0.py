class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c=collections.Counter(arr)
        maxi=-1
        for i in c:
            if i==c[i]:
                maxi=max(maxi,i)
        return maxi
