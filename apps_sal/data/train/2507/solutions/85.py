class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        # Method 1:
        letters = {}
        for char in chars:
            letters[char] = letters.get(char, 0) + 1

        count = 0
        for word in words:
            tmp = letters.copy()
            flag = 1
            for char in word:
                if char in tmp and tmp[char] >= 1:
                    tmp[char] -= 1
                else:
                    flag = 0
                    break
            if flag:
                count += len(word)
        return count
