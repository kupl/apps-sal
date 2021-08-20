class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        out = 0
        for word in words:
            cnt = 0
            for letter in word:
                if letter in chars and word.count(letter) <= chars.count(letter):
                    cnt += 1
            if cnt == len(word):
                out += len(word)
        return out
