class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        l=list(set(arr))
        for i in range(len(l)):
            l[i]=arr.count(l[i])
        if len(l)==len(set(l)):
            return True
        else:
            return False
        

