class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = []
        for word in words:
            count = 0
            for char in word:
                if char in chars and word.count(char) <= chars.count(char):
                    count += 1
            if count == len(word):
                res.append(count)

        return sum(res)
