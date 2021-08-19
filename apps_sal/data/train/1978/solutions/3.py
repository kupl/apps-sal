class Solution:

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        output = []
        for word in words:
            (fwd, reverse, valid) = (defaultdict(str), defaultdict(str), True)
            for i in range(len(word)):
                if word[i] not in fwd and pattern[i] not in reverse:
                    fwd[word[i]] = pattern[i]
                    reverse[pattern[i]] = word[i]
                else:
                    valid = fwd[word[i]] == pattern[i] and reverse[pattern[i]] == word[i]
                if not valid:
                    break
            if valid:
                output.append(word)
        return output
