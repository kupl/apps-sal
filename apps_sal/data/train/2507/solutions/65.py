class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # first solution
        register = {}
        for char in chars: register[char] = register.get(char, 0) + 1
        result = 0
        for word in words:
            temp = {}
            for char in word: temp[char] = temp.get(char, 0) + 1
            for char, num in list(temp.items()):
                if temp[char] > register.get(char, 0):
                    break
            else:
                result+=len(word)
        return result

