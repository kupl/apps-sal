class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        d = dict()
        for char in chars:
            d[char] = d.get(char, 0) + 1
        for word in words:
            c = dict()
            for char in word:
                c[char] = c.get(char, 0) + 1
            bad = False
            while c and (not bad):
                char = c.popitem()
                if char[0] in d and d[char[0]] >= char[1]:
                    continue
                else:
                    bad = True
            if not bad:
                res += len(word)
        return res
