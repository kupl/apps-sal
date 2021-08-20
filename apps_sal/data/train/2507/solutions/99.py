class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        dic = collections.Counter(chars)
        for word in words:
            passed = True
            for ch in word:
                if dic[ch] < word.count(ch):
                    passed = False
            if passed:
                count += len(word)
        return count
