class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        setChars = set(chars)
        counts = [0] * len(setChars)
        map = {}
        res = 0
        for (i, val) in enumerate(setChars):
            map[val] = i
        for (i, val) in enumerate(chars):
            counts[map.get(val)] += 1
        for word in words:
            tempCounts = counts[:]
            flag = 1
            for char in word:
                index = map.get(char, -1)
                if index == -1:
                    flag = 0
                    continue
                tempCounts[index] -= 1
                if tempCounts[index] < 0:
                    flag = 0
                    continue
            if flag:
                res += len(word)
        return res
