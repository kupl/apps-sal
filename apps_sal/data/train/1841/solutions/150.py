import math
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        print(len(arr))
        m = arr[math.ceil(len(arr)/2)-1]
        print(m)
        n = len(arr)
        for i in range(n) :
            arr[i] = [abs(arr[i]-m),arr[i]]
        arr.sort(reverse=True)
        arr = arr[:k]
        for i in range(k) :
            arr[i] = arr[i][1]
        return arr
