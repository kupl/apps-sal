class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        ans = 0
        for word in words:

            charscopy = [i for i in chars]
            length = 0
            for char in word:
                if char in charscopy:
                    length += 1
                    charscopy.remove(char)

            if length == len(word):
                ans += length

        return ans
