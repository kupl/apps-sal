class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        import copy
        total = 0
        y = {}
        for char in chars:
            if char in y:
                y[char] += 1
            else:
                y[char] = 1
        for word in words:
            x = copy.deepcopy(y)
            temp = 0
            for char in word:
                if char in x and x[char] > 0:
                    x[char] -= 1
                    temp += 1
                else:
                    temp = 0
                    break
            total += temp
        return total
