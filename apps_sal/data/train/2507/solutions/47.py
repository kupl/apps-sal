class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        d_chars = Counter(chars)
        ans = 0
        for w in words:
            d_w = Counter(w)
            for (k, v) in d_w.items():
                if d_chars[k] < v:
                    break
            else:
                ans += len(w)
        return ans
