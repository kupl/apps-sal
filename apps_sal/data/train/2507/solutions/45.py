class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        mp = Counter(chars)
        for word in words:
            ok = True
            mp_word = Counter(word)
            for (ch, f) in mp_word.items():
                if ch not in mp or mp_word[ch] > mp[ch]:
                    ok = False
                    break
            if ok:
                ans += len(word)
        return ans
