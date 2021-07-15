class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        indexer = len(arr) 
        for i in range(indexer):
            for j in range(1, indexer - i):
                for k in range(1, indexer - i - j):
                    if abs(arr[i] - arr[i + j]) <= a:
                        if abs(arr[i + j] - arr[i + j + k]) <= b:
                            if abs(arr[i] - arr[i + j + k]) <= c:
                                count += 1
                                
        
        
        
        return count
