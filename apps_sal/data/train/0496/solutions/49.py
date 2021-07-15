class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        counter = Counter(A)
        to_place = []
        
        min_key = float('inf')
        for key in counter:
            min_key = min(min_key, key)
            if counter[key] > 1:
                for i in range(counter[key] - 1):
                    to_place.append(key)
                counter[key] = 1
        
        i = min_key
        moves = 0 
        to_place.sort(reverse=True)
        
        while to_place:
            if i not in counter and i > to_place[-1]:
                moves += i - to_place.pop()
            i += 1
        return moves
    
    # [3,2,1,2,1,7]
    
    # counter:{1:1, 2:1, 5:1, 7:1}
    # to_place =[5, 1]
    # i = 6
    # moves =  

