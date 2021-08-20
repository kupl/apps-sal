class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = 0
        for i in words:
            a = i
            for j in chars:
                if j in a:
                    a = a[:a.index(j)] + a[a.index(j) + 1:]
            if len(a) == 0:
                counter += len(i)
        return counter
