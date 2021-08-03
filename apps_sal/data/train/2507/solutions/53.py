class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        tot = 0
        for w in words:
            d = {}
            for c in chars:
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1
            temp = 0
            for l in w:
                if l in d and d[l] > 0:
                    d[l] -= 1
                    temp += 1
                else:
                    temp = 0
                    break

            tot += temp

        return tot
