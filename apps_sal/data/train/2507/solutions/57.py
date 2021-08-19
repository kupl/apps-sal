class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        '''
        # first solution
        register = {}
        for char in chars: register[char] = register.get(char, 0) + 1
        result = 0
        for word in words:
            temp = {}
            for char in word: temp[char] = temp.get(char, 0) + 1
            for char, num in temp.items():
                if temp[char] > register.get(char, 0):
                    break
            else:
                result+=len(word)
        return result
        '''
        # second solution
        tot = 0
        for w in words:
            d = {}
            for c in chars:
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1

            temp = 0
            for l in w:
                if l in d and d[l] > 0:
                    d[l] -= 1
                    temp += 1
                else:
                    temp = 0
                    break

            tot += temp

        return tot
