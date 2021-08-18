class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        orda = ord('a')
        mask = defaultdict(int)

        for w in words:
            m = 0
            for c in w:
                m |= 1 << (ord(c) - orda)
            mask[m] += 1

        res = []
        for p in puzzles:
            ones = []
            for c in p:
                ones.append(1 << (ord(c) - orda))

            valid = [ones[0]]
            for i in range(1, 7):
                valid.extend([ones[i] + v for v in valid])

            novw = 0
            for v in valid:
                if v in mask:
                    novw += mask[v]
            res.append(novw)
        return res
