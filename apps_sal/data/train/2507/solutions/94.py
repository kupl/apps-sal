class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        myd = {}
        count = 0
        for i in chars:
            if i in myd.keys():
                myd[i] += 1
            else:
                myd[i] = 1

        for word in words:
            allin = True

            for letter in word:
                if letter in myd.keys():
                    if word.count(letter) > myd[letter]:
                        allin = False
                else:
                    allin = False
            if allin == True:
                count += len(word)
        return count
