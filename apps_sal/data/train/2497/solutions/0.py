class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        flag = False
        odd = 0
        i = 0
        while i < len(arr):
            if arr[i] % 2 == 1:
                if not flag:
                    flag = True
                    odd += 1
                    i += 1
                else:
                    odd += 1
                    i += 1
            else:
                if not flag:
                    i += 1
                else:
                    flag = False
                    odd = 0
                    i+= 1
                    
            if odd == 3:
                return True
            
        return False
            
                    

