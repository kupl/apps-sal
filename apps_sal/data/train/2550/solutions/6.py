class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        cnt10Bill, cnt20Bill, cnt5Bill = 0, 0, 0
        for b in bills:
            if b == 5:
                cnt5Bill += 1
            elif b == 10:
                cnt10Bill += 1
                if cnt5Bill >= 1:
                    cnt5Bill -= 1
                else:
                    return False
                
            elif b == 20:
                cnt20Bill += 1
                if cnt5Bill >= 1 and cnt10Bill >= 1:
                    cnt5Bill -= 1
                    cnt10Bill -= 1
                elif cnt5Bill >= 3:
                    cnt5Bill -= 3
                else:
                    return False
            print((cnt5Bill, cnt10Bill, cnt20Bill))
        return True
    
                
                
                

