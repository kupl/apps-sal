class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        number_of_cons_odds = 0
        
        for elem in arr:
            if elem % 2 == 0:
                number_of_cons_odds = 0
                continue
            
            number_of_cons_odds += 1
            if number_of_cons_odds == 3:
                return True
            
        return False
