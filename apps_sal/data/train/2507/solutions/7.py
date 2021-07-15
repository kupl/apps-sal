class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum = 0
        for i in words:
            check = True
            for s in i:
                if i.count(s) > chars.count(s):
                    check = False
            if check == True:
                sum = sum + len(i)
        return sum
