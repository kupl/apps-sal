class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ij = {}
        total = 0
        
        for q in range(len(arr) - 1):
            for r in range(q + 1, len(arr)):
                v = abs(arr[q] - arr[r])
                
                if v <= a:
                    if r in ij:
                        ij[r].append(q)
                    else:
                        ij[r] = [q] # r = j, q = i
                if v <= b: # q = j, r = k, ij[q] = i
                    if q in ij:
                        for i in ij[q]:
                            if abs(arr[i] - arr[r]) <= c:
                                total += 1
                        
        
        return total
