class Solution:
    def divisorGame(self, N: int) -> bool:
        
        def divisors(N):
            if N == 1:
                return [1]
            
            res = []
            for n in range(1, int(N**0.5)+1):
                if N % n == 0:
                    res.append(n)
            return res
        
        # Initial conditions
        table = {
            1 : False,
            2 : True,
            3 : False
        }
        
        def compute(i):
            if i in table:
                return table[i]
            
            divs = divisors(i)
            next_nums = [i-d for d in divs]
            
            for n in next_nums:
                status = compute(n)
                
                if status == False:
                    table[i] = True
                    return True
            table[i] = False
            return False
        
        
#         for n in range(3, N+1):
#             divs = divisors(n)
            
#             for d in divs:
#                 next_num = n - d
#                 if table[next_num] == False:
#                     # We want the next number to be a losing number
#                     table[n] = True
#                     break
#             if n not in table:
#                 # If all next numbers are winning, then this is a losing number
#                 table[n] = False

        return compute(N)
