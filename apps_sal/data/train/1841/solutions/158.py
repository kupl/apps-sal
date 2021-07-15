class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = arr[(len(arr)-1)//2]
        #print(median)
        arr.sort(key = lambda x: (abs(x-median),x),reverse = True)
        #print(arr)
        return arr[:k]

