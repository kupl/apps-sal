class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = {5: 0, 10: 0, 20:0}
    
        for i in bills:
            cash[i] += 1 
            if i - 5 == 15: 
                if (cash[5] < 3) and (cash[10] < 1  or cash[5] < 1 ): 
                    print('false')
                    return False
                else: 
                    if cash[10] >= 1 and cash[5] >= 1 : 
                        cash[10] -= 1
                        cash[5] -= 1
                    elif cash[5] >= 3:
                        cash[5] -= 3
                
            if i - 5 == 5:
                if cash[5] < 1: 
                    print('false')
                    return False 
                else:
                    cash[5] -= 1 
        return True 
            
             

