class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        start = 0
        for i in words:
            count = 0
            t = list(chars)
            for j in i:
                if j in t:
                    count += 1
                    t.remove(j)
            if count == len(i):
                start += count
        return start
