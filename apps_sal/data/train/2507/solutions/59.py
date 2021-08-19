class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        cCounter = collections.Counter(chars)
        sum = 0
        for word in words:
            wCounter = collections.Counter(word)
            match = True
            for (k, v) in wCounter.items():
                if cCounter[k] < v:
                    match = False
            if match:
                sum += len(word)
        return sum
