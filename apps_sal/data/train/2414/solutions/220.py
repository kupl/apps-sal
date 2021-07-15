class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cnt = 0
        length = len(arr)
        
        for idx in range(length):
            first = arr[idx]
            
            for ydx in range(idx+1,length):
                second = arr[ydx]
                
                if abs(first-second) <= a:
                    
                    for kdx in range(ydx+1, length):
                        third = arr[kdx]
                        
                        if abs(first-third) <= c and abs(second-third) <= b:
                                    cnt += 1
        return cnt

