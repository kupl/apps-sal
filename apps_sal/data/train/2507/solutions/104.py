class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = defaultdict(int)

        for l in chars:
            freq[l] += 1

        count = 0
        for word in words:
            testFreq = freq.copy()
            match = True
            for letter in word:
                if testFreq[letter] <= 0:
                    match = False
                    break
                testFreq[letter] -= 1
            if match:
                count += len(word)

        return count
