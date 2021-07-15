class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        k=list(set(arr))
        tmp=[]
        for i in k:
            tmp.append(arr.count(i))
        max1=max(tmp)
        index=tmp.index(max1)
        print(k[index])
        if max1>(len(arr)/4):
            return k[index]
