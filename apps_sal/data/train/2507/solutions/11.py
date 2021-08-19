class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        output = 0
        add = True
        for word in words:
            for c in word:
                if word.count(c) > chars.count(c):
                    add = False
            if add:
                output += len(word)
            else:
                add = True
        return output
