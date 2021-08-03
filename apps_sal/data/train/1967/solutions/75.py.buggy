class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        
        S_len = len(S)
        res = []
        prev = None
        
        def check(index, prev_back, prev):
            if index == S_len:
                return ['#']
            
            buffer = \"\"
            
            for i in range(index, S_len, 1):
                
                if S[index] == '0' and i - index > 0:
                    break
                
                buffer += S[i]
                buffer_int = int(buffer)
                
                if buffer_int > 2**31 - 1:
                    break
                
                if buffer_int == prev_back + prev:
                    x = check(i + 1, prev, buffer_int)
                    if x:
                        return [buffer_int] + x
                    
                elif buffer_int > prev_back + prev:
                    break
                    
            return []
        
        for i in range(0, S_len - 2, 1):
            
            if S[0] == '0' and i + 1 > 1:
                break
            
            for j in range(i+1, S_len - 1, 1):
                
                if S[i+1] == '0' and j - i > 1:
                    break
                
                prev_back = int(S[:i + 1])
                prev = int(S[i+1 : j+1])
                
                x = check(j + 1, prev_back, prev)
                if x:
                    return [prev_back, prev] + x[:-1]
                
            
        return []
                
