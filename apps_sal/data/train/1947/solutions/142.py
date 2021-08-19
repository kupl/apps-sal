class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        s = set(A)
        letters_required = {}
        for b in B:
            for c in b:
                count = b.count(c)
                if c not in letters_required or count > letters_required[c]:
                    letters_required[c] = count
        for a in A:
            for lr in letters_required:
                if a.count(lr) < letters_required[lr]:
                    s.remove(a)
                    break
        return list(s)
