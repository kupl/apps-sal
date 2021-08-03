class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charChars = Counter(chars)
        counter = 0
        for word in words:
            countC = Counter(word)
            count = 0
            for letter in countC.items():
                if letter[0] in charChars and charChars[letter[0]] >= letter[1]:
                    count += 1

            if count == len(countC):
                counter += len(word)
        return counter
