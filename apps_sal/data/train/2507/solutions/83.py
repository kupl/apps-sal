from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c_c = Counter(chars)
        good_w = []
        for w in words:
            w_c = Counter(w)
            sampled_w = ''.join([c for c in w if c_c[c] >= w_c[c]])
            if w == sampled_w:
                good_w.append(w)
        return sum(len(w) for w in good_w)
