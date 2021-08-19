from collections import defaultdict


class Solution:

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        tri = defaultdict(lambda: 0)
        for word in words:
            cur = tri
            letters = sorted(set(word))
            for i in range(len(letters)):
                if letters[i] in cur:
                    cur = cur[letters[i]]
                else:
                    cur[letters[i]] = defaultdict(lambda: 0)
                    cur = cur[letters[i]]
                if i == len(letters) - 1:
                    if '*' in cur:
                        cur['*'] += 1
                    else:
                        cur['*'] = 1
        returnArr = [0] * len(puzzles)

        def helper(tri, puzzle, i, found_first):
            firstLetter = puzzle[0]
            if '*' in tri and found_first:
                returnArr[i] += tri['*']
            for letter in tri:
                if letter in puzzle:
                    if firstLetter == letter or found_first:
                        helper(tri[letter], puzzle, i, True)
                    else:
                        helper(tri[letter], puzzle, i, False)
        for i in range(len(puzzles)):
            helper(tri, puzzles[i], i, False)
        return returnArr
