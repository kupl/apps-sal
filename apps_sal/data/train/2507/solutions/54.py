class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        ans = 0
        for word in words:

            charscopy = [i for i in chars]
            length = 0
            for char in word:
                if char not in charscopy:
                    break
                charscopy.remove(char)
            else:
                ans += len(word)

        return ans
