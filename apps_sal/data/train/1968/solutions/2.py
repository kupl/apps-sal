class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        return self.first_implementation(folder)
    
    def first_implementation(self, folder: List[str]) -> List[str]:
        \"\"\"
        The directories are not guaranteed to be in sorted order. Sort the input in place with heapsort O(n log n) 
        If they are then this problem goes into O(n) Time
        Benefit of sorting time goes from O(n^2) to O(n log n).
        
        Iterate over the sorted array finding common roots. As long as the next item's root is in the previous 
        remove it.
        \"\"\"
        if not folder:
            return []
        from heapq import heapify, heappop
        heapify(folder)
        # initialize the output though it could be done in true O(1) space with peaking at
        # the previous element in the heap but that would require a pop push
        result = [heappop(folder)]
        
        while folder:
            cur = heappop(folder)
            if not cur.startswith(result[-1] + '/'):
                result.append(cur)
        
        return result
        
        
