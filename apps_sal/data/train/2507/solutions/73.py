class Solution:

    def countCharacters(self, words, chars):
        sum = 0
        count = {}
        for c in chars:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        for word in words:
            seen = {}
            validWord = True
            for c in word:
                if c in seen:
                    seen[c] += 1
                else:
                    seen[c] = 1
                if c not in count or seen[c] > count[c]:
                    validWord = False
            if validWord:
                sum += len(word)
        return sum
