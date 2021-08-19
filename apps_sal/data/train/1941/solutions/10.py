class Solution:

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        wdict = defaultdict(int)

        def getbitmask(word):
            mask = 0
            for w in word:
                i = ord(w) - ord('a')
                mask |= 1 << i
            return mask
        op = [0] * len(puzzles)
        for word in words:
            mask = getbitmask(word)
            wdict[mask] += 1
        for (i, pz) in enumerate(puzzles):
            mask = getbitmask(pz)
            fi = ord(pz[0]) - ord('a')
            submask = mask
            count = 0
            while True:
                if submask >> fi & 1:
                    count += wdict[submask]
                if submask == 0:
                    break
                submask = submask - 1 & mask
            op[i] = count
        return op
