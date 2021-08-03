class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        total = 0
        for word in words:
            mod_chars = list(chars)
            found = 0
            for c in word:
                if c in mod_chars:
                    del mod_chars[mod_chars.index(c)]
                    found += 1
            if found == len(word):
                total += found

        return total
