class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n=len(arr)
        arr=sorted(arr)
        m=-1
        if(n%2==0):
            m=arr[(n-1)//2]
        else:
            m=arr[n//2]
        # print(arr)
        # print(m)
        arr=sorted(arr,key=lambda x:(abs(x-m),x))
        # print(arr)
        return arr[-k:]
