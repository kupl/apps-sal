class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsDict = {}
        for char in chars:
            if char not in charsDict:
                charsDict[char] = 0
            charsDict[char] += 1

        ans = 0

        for word in words:
            tempDict = charsDict.copy()
            isGood = True
            for char in word:
                if char not in tempDict:
                    isGood = False
                    continue
                else:
                    if tempDict[char] == 0:
                        isGood = False
                        continue

                    else:
                        tempDict[char] -= 1

            if isGood:
                ans += len(word)

        return ans
