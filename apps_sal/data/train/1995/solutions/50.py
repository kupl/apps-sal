class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        \"\"\"
        [[2,1,5],[3,3,7]]
        
        1 2 3 4 5 6 7
        2 2 2 2 2
        2 2 5 2 2        
        
        c = 4
        \"\"\"
            
        count_vec = [0]*1001
                        
        for num_pass, start, end in trips:
            for i in range(start, end):
                count_vec[i] += num_pass
                if count_vec[i] > capacity:
                    return False
                
        return True
        
