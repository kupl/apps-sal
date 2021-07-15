class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        b_chars = defaultdict(int)
        for b in B:
            chars = Counter(b)
            for c in b:
                b_chars[c] = max(b_chars[c], chars[c])
        output = []
        for a in A:
            a_chars = Counter(a)
            if all(a_chars[c] >= b_chars[c] for c in b_chars):
                output.append(a)    
        return output
