class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        count = collections.Counter(frozenset(w) for w in words)
        res = []
        for p in puzzles:
            cur = 0
            for k in range(7):
                for c in itertools.combinations(p[1:], k):
                    cur += count[frozenset(tuple(p[0]) + c)]
            res.append(cur)
        return res

    def findNumOfValidWords2(self, words, puzzles):
        count = collections.Counter()
        for w in words:
            if len(set(w)) > 7: continue
            m = 0
            for c in w:
                m |= 1 << (ord(c) - 97)
            count[m] += 1
        res = []
        for p in puzzles:
            bfs = [1 << (ord(p[0]) - 97)]
            for c in p[1:]:
                bfs += [m | 1 << (ord(c) - 97) for m in bfs]
            res.append(sum(count[m] for m in bfs))
        return res
    
    def getBitMask(self, word: str) -> int:
        mask = 0
        for c in word:
\t\t    # Maps 'a' -> 0, 'b' -> 1, 'c' -> 2, ...
            i = ord(c) - ord('a')
\t\t\t# Sets the i-th bit to 1.
            mask |= 1 << i
        return mask

    def findNumOfValidWords1(self, words: List[str], puzzles: List[str]) -> List[int]:
\t    # [2]
\t\t# Maps the bit mask for every word to the count of words with that same bit mask.
\t\t# For example 'abd' and 'baddd' would have the same mask because they are composed
\t\t# of the same set of characters.
        letterFrequencies = {}
        for word in words:
            mask = self.getBitMask(word)
            letterFrequencies[mask] = letterFrequencies.get(mask, 0) + 1
        
        solution = [0] * len(puzzles)
        
        for i in range(len(puzzles)):
            puzzle = puzzles[i]
            mask = self.getBitMask(puzzle)
            subMask = mask
            total = 0
\t\t\t
\t\t\t# The index of the first bit in the puzzle. We need this to check if the
\t\t\t# submasks we generate are of valid words.
            firstBitIndex = ord(puzzle[0]) - ord('a')

\t\t\t# [3]
            # In this while loop we want to go through all possible \"submasks\" of the bit
\t\t\t# mask for the current puzzle. If our puzzle bit mask is 1011, for example, we
\t\t\t# would generate 1011, 1010, 1001, 1000, 0011, 0010, 0001, 0000
            while True:
\t\t\t\t# [4]
\t\t\t    # If this submask contains the first letter of the puzzle, it's a valid word. Here
\t\t\t\t# we add to the number of words we've seen with this mask to our total.
                if subMask >> firstBitIndex & 1:
                    total += letterFrequencies.get(subMask, 0)
\t\t\t\t# We've exhausted all possible submasks.
                if subMask == 0:
                    break
\t\t\t\t# Get rid of the right-most bit, and restore any bits to the right of it that were
\t\t\t\t# originally in the mask. If the original mask was '01011' current submask is '01000',
\t\t\t\t# then submask - 1 = '00111' and (submask - 1) & mask = '00011'.
                subMask = (subMask - 1) & mask
            solution[i] = total
        
        return solution
