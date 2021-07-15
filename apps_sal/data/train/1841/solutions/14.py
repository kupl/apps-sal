class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        res=[]
        val=arr[(len(arr)-1)//2]
        arr.sort(key=lambda x: (abs(x-val),x),reverse=True)
        return arr[:k]
