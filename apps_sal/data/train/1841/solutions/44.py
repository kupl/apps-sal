class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        sorted_arr = sorted(arr)
        m = sorted_arr[(len(arr)-1)//2]
        
        num_dist = [(e,abs(e-m)) for e in sorted_arr]
        num_dist.sort(key=lambda x:x[0],reverse=True)
        num_dist.sort(key=lambda x:x[1],reverse=True)
        
        ans = [e[0] for e in num_dist]
        return ans[:k]
