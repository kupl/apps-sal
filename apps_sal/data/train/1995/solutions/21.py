class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    
        def Sort(sub_li): 
            sub_li.sort(key = lambda x: x[1]) 
            return sub_li 
        
        trips = Sort(trips)
        
        people = 0
        on_board = []
        
        for [n,a,b] in trips:
            people +=n
            
            while on_board and on_board[0][1]<=a:
                t = on_board.pop(0)
                people -= t[0]
                
            if people>capacity:
                return False
            
            on_board.append([n,b])
            on_board = Sort(on_board)
            
        return True
