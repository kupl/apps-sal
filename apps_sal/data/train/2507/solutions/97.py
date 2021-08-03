class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        length = 0

        m = Counter(chars)

        for word in words:

            passed = True

            for char in word:

                if m[char] < word.count(char):

                    passed = False

            if passed:

                length += len(word)

        return length
