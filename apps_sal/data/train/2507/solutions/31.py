import copy


class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        charmap = dict()
        for c in chars:
            if c in charmap:
                charmap[c] += 1
            else:
                charmap[c] = 1
        size = 0
        for word in words:
            temp = copy.deepcopy(charmap)
            flag = True
            for c in word:
                if c in temp and temp[c] > 0:
                    temp[c] -= 1
                else:
                    flag = False
                    break
            if flag:
                size += len(word)
        return size
