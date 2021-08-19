class Solution:

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # 97 = ord('a')

        def wordToInt(word: str) -> int:
            n = 0
            ls = 0
            for c in word:
                cn = 1 << (ord(c) - 97)
                ls += 1 if cn & n == 0 else 0
                if ls > 7:
                    return None
                n |= cn
            return n

        def validWords(ws, puzzle: str) -> int:
            return sum((ws[n] if n in ws else 0) for n in getPossibleNums(puzzle, 0))

        def getPossibleNums(puzzle: str, i: int) -> List[int]:
            cn = 1 << (ord(puzzle[i]) - 97)
            if i == len(puzzle) - 1:
                return [cn, 0]
            elif i == 0:
                return [n | cn for n in getPossibleNums(puzzle, 1)]
            else:
                tmp = getPossibleNums(puzzle, i + 1)
                return [n | cn for n in tmp] + tmp

        ws = {}
        for w in words:
            n = wordToInt(w)
            if n is not None:
                ws[n] = 1 + (ws[n] if n in ws else 0)

        return list(map(lambda p: validWords(ws, p), puzzles))
