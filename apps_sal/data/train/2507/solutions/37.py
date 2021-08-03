class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        out = 0

        for word in words:
            good = True

            for char in word:
                if word.count(char) > chars.count(char):
                    good = False

            if good:
                out += len(word)

        return out
