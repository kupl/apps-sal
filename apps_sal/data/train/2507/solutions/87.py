class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for word in words:
            c = collections.Counter(chars)
            add = True
            for letter in word:
                if c[letter] > 0:
                    c[letter] -= 1
                else:
                    add = False
            if add == True:
                ans += len(word)
        return ans
