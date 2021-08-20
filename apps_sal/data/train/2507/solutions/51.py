class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        dtar = Counter(chars)
        for i in range(len(words)):
            for j in words[i]:
                if j not in dtar:
                    break
                if words[i].count(j) > 1:
                    if words[i].count(j) > dtar[j]:
                        break
            else:
                res += len(words[i])
        return res
