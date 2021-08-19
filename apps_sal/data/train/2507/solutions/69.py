class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:

        def strToList(word):
            return [char for char in word]

        def canForm(word, bank):
            tmp = word
            while tmp != []:
                x = tmp[0]
                tmp.remove(tmp[0])
                if x in bank:
                    bank.remove(x)
                else:
                    return False
            return True
        totalLen = 0
        for word in words:
            bank = strToList(chars)
            wordAsList = strToList(word)
            if canForm(wordAsList, bank):
                totalLen += len(word)
        return totalLen
