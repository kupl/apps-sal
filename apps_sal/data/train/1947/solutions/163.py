class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        #Time Complexity: O(A+B), where A and B is the total amount of letters in A and B respectively.
        #Space O(A.length + B).
        if not B:
            return A
        
        mapB = collections.defaultdict(int) #max required number of each letter of all words in B
        for b in B:
            counter = collections.Counter(b)
            for k in counter:
                mapB[k] = max(counter[k], mapB[k])
        
        
        res = []
        for a in A:
            countA = collections.Counter(a)
            if all(countA[ch] >= mapB[ch] for ch in mapB ):
                res.append(a)
            
            
        return res
                
                
                    
                    

