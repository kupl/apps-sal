from collections import Counter


class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        d = Counter(chars)
        cnt = [Counter(w) for w in words]
        ans = 0
        for (i, x) in enumerate(cnt):
            found = True
            print(x)
            for k in x:
                if k not in d or x[k] > d[k]:
                    found = False
                    break
            if found:
                ans += len(words[i])
        return ans
