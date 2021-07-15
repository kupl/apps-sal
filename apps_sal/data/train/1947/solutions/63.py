class Solution:
    
    def getCharFrequency(self, word):
        
        f = [0] * 26        
        for ch in word:            
            f[ord(ch)-ord('a')] += 1
        
        return f
            
        
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        result = []
        
        max_freq = [0]* 26
        
        for i in range(len(B)):
            curr_freq = self.getCharFrequency(B[i])
            
            for j in range(26):
                max_freq[j] = max(max_freq[j], curr_freq[j])
    
        
        for i in range(len(A)):
            curr_freq = self.getCharFrequency(A[i])
            
            valid = True
            
            for j in range(26):
                if max_freq[j] > curr_freq[j]:
                    valid = False
                    break
                
            if valid:
                result.append(A[i])
        
        return result
    
    
    

