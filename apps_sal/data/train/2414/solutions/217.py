class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        ans = []
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    ij = abs(arr[i] - arr[j])
                    jk = abs(arr[j] - arr[k])
                    ik = abs(arr[i] - arr[k])
                    if ij <= a and jk <= b and ik <= c:
                        ans.append([arr[i], arr[j], arr[k]])
        
        return len(ans)
