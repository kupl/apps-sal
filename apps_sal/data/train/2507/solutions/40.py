class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        a = 0
        for word in words:
            res = True
            for i in word:
                if word.count(i) > chars.count(i):
                    res = False
                    break
            if res:
                a += len(word)
        return a
