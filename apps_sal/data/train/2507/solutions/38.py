class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charBins = {char: chars.count(char) for char in chars}
        goodWords = []

        for word in words:
            if (len(word) > len(chars)):
                continue

            if not set(word).issubset(chars):
                continue

            letterBins = {letter: word.count(letter) for letter in word}
            if min([letterBins[letter] <= charBins[letter] for letter in letterBins]):
                goodWords.append(word)

        return sum(len(word) for word in goodWords)
