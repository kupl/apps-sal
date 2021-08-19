class Solution:

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:

        def getNum(s: str) -> int:
            res = 0
            for c in s:
                res |= 1 << ord(c) - 97
            return res
        counter = Counter([getNum(set(word)) for word in words if len(set(word)) < 8])
        ans = []
        for puzzle in puzzles:
            sub = [1 << ord(puzzle[0]) - 97]
            for c in puzzle[1:]:
                sub += [m | 1 << ord(c) - 97 for m in sub]
            ans.append(sum((counter[w] for w in sub)))
        return ans
