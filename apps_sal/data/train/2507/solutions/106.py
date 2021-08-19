class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        sum = 0
        p = 0
        for th in words:
            for i in range(len(th)):
                if th[i] in chars:
                    if th.count(th[i]) <= chars.count(th[i]):
                        p = p + 1
            if p == len(th):
                sum = sum + p
            p = 0
        return sum
