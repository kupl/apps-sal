from queue import PriorityQueue

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sorted_trips = sorted(trips, key=lambda x: (x[1], x[2]))        
        pq = PriorityQueue()
        total_pnum = 0
        
        for trip in sorted_trips:
            pnum, start_loc, end_loc = trip[0], trip[1], trip[2]            
            total_pnum += pnum   
            
            while pq.qsize() > 0:
                prev_end_loc, prev_pnum = pq.get()
                if prev_end_loc > start_loc:                    
                    pq.put((prev_end_loc, prev_pnum))
                    break                    
                total_pnum -= prev_pnum                
                
            if end_loc > start_loc: 
                pq.put((end_loc, pnum))
                
            if total_pnum > capacity: 
                return False
            
        return True

# Time complexity: O(nlogn)
# Time complexity: O(n) for the priorioty queue

