class Solution:
    def get_values(self, s, idx):
        for i in range(idx, len(s)):
            yield (i, s[idx:i+1])
        
    def splitIntoFibonacci(self, S: str) -> List[int]:
        for i, a in self.get_values(S, 0):
            if a != '0' and a.startswith('0'): break
            for j, b in self.get_values(S, i+1):
                if b != '0' and b.startswith('0'): break
                k = j+1
                out = [a,b]
                while k < len(S):
                    v = int(a) + int(b)
                    str_v = str(v)
                    if v <= 2**31 - 1 and S[k:].startswith(str_v):
                        k = k + len(str_v)
                        a, b  = b, str_v
                        out.append(v)
                    else:
                        break
                if len(out) >= 3:                        
                    if len(''.join(map(str, out))) == len(S):
                         return out
        return [] 
                
            

