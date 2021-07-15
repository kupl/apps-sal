class Solution:
    \"\"\"
    [\"amazon\",\"apple\",\"facebook\",\"google\",\"leetcode\"]
    [\"lo\",\"eo\"]
    Expected: [\"google\",\"leetcode\"]
        
    [\"amazon\",\"apple\",\"facebook\",\"google\",\"leetcode\"]
    [\"e\",\"o\"]
    Expected: [\"facebook\",\"google\",\"leetcode\"]
    
    [\"amazon\",\"apple\",\"facebook\",\"google\",\"leetcode\"]
    [\"e\",\"oo\"]
    [\"facebook\",\"google\"]
    \"\"\"
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        bchars = collections.defaultdict(int)
        for b in B:
            bcount = collections.Counter(b)
            for key in bcount:
                bchars[key] = max(bchars[key], bcount[key])
        result=[]
        for a in A:
            achars = collections.Counter(a)
            subset = True
            for c in bchars:
                if bchars[c] <= achars[c]:
                    continue
                else:
                    subset = False
                    
            if subset:
                result.append(a)
        return result
