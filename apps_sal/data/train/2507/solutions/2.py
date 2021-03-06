class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        charBins = {char: chars.count(char) for char in chars}
        total = 0
        for word in words:
            if len(word) > len(chars):
                continue
            if not set(word).issubset(chars):
                continue
            letterBins = {letter: word.count(letter) for letter in word}
            goodWord = True
            for letter in letterBins:
                if letterBins[letter] > charBins[letter]:
                    goodWord = False
            if goodWord:
                total += len(word)
        return total
