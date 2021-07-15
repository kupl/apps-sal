from collections import defaultdict
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        b_dict = defaultdict(int)
        for word in B:
            curr = defaultdict(int)
            for char in word:
                curr[char] += 1
            for char in curr:
                b_dict[char] = max(b_dict[char], curr[char])
        
        universal = []
        for word in A:
            curr = defaultdict(int)
            for char in word:
                curr[char] += 1
            
            is_subset = True
            for char in b_dict:
                if char not in curr or curr[char] < b_dict[char]:
                    is_subset = False
                    break
            if is_subset:
                universal.append(word)
                
        return universal
    
        # len(A) = n, len(B) = m, word len = 10, time: 10m + 10n + 26 = O(m + n)
    

