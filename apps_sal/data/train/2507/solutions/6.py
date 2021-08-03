class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        num = 0

        for word in words:
            letter = str()
            counter = Counter(chars)
            for i in word:
                if i in list(counter.keys()) and counter[i] > 0:
                    letter += i
                    counter[i] -= 1

            if letter == word:
                print(letter)
                num += len(word)
        return num
