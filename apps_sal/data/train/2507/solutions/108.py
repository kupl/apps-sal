class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        sum_ = 0
        for word in words:
            s = Counter(chars)
            flag = 0
            for letter in word:
                if letter in list(s.keys()) and s[letter] != 0:
                    s[letter] -= 1
                else:
                    flag = 1
            if flag == 0:
                sum_ += len(word)
        return sum_
