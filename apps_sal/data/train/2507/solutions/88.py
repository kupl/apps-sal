class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        cmap = {ch: chars.count(ch) for ch in chars}
        for word in words:
            wmap = {ch: word.count(ch) for ch in word}
            count_me_in = True
            for (k, v) in wmap.items():
                try:
                    v1 = cmap[k]
                    if v1 < v:
                        raise Exception('Frequency not enough!')
                except:
                    count_me_in = False
                    break
            if count_me_in:
                ans += len(word)
        return ans
