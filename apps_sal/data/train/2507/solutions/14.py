class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        res = 0
        for j in words:
            tmp = Counter(j) & Counter(chars)
            if tmp == Counter(j):
                res += len(j)
        return(res)
