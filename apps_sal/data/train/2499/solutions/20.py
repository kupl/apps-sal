def compute_gcd(a, b):
    if(b == 0):
        return a 
    else:
        return compute_gcd(b, a % b)

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        max_size = int(1e4 + 1)
        n = len(deck)
        freq = [0 for _ in range(max_size)]
        
        for i in range(n):
            freq[deck[i]] += 1
        
        gcd = freq[deck[0]]
        
        for i in range(max_size):
            gcd = compute_gcd(gcd, freq[i])
        
        if gcd == 1: return False
        
        return True
