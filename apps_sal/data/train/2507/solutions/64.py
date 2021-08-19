class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        out = 0
        chars = list(chars)
        for i in words:
            f = 0
            temp = chars[:]
            for j in i:
                if j in temp:
                    temp.remove(j)
                else:
                    f = 1
                    break
            if f == 0:
                out += len(i)
        return out
