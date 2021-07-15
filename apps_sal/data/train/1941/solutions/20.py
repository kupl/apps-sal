class Solution:
    wdMap = {}
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        res = []
        self.wdMap = self.hashwords(words)
        for puzzle in puzzles:
            res.append(self.checkValidWord(puzzle, 0, 0))

        return res

    def checkValidWord(self, puzzle, i, id):
        if i == len(puzzle):
            return self.wdMap.get(id , 0)
        indx = ord(puzzle[i]) - ord('a')
        nextid = id | (1<<indx)
        if i == 0:
            return self.checkValidWord(puzzle, i + 1, nextid)
        else:
            return self.checkValidWord(puzzle, i + 1, id) + self.checkValidWord(puzzle, i+1, nextid)


    def hashwords(self, words):
        wdMap = {}
        for word in words:
            letter_id = 0
            for letter in word:
                indx = ord(letter) - ord('a')
                letter_id = letter_id | (1 << indx)
            wdMap[letter_id] = wdMap.get(letter_id, 0) + 1
        return wdMap

