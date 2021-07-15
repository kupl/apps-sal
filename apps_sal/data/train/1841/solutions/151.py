class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        sort_arr = sorted(arr)
        n = len(arr)
        m = sort_arr[((n-1))//2]
        result = sorted(sort_arr, key = lambda x : [abs(x - m),x], reverse = True)
        return result[0:k]
        

