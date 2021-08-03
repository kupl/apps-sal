class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # O(m + n); m and n is the total amount of chars in A and B
        def count(word):
            counter = [0] * 26
            for w in word:
                counter[ord(w) - ord(\"a\")] += 1
            return counter
            
        b_char_combine = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                b_char_combine[i] = max(b_char_combine[i], c)

        res = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), b_char_combine)):
                res.append(a)

        return res
            
