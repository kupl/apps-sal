from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = 'balloon'
        arr = []
        dic = Counter(list(text))
        for c in word:
            arr.append(dic[c]//word.count(c))
        return min(arr)
