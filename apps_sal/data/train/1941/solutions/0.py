class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # 1st step
        # construct a mask for each word
        # note that there may be duplicate mask for different words
        # so we need a dict to count the number
        orda = ord('a') # 97
        mask = defaultdict(int) # word mask
        
        for w in words:
            m = 0
            for c in w:
                m |= 1 << (ord(c) - orda)
            mask[m] += 1
        
        # 2nd step
        # for each puzzle, construct the corresponding mask for each possible valid word, check whether the word is in mask
        res = []
        for p in puzzles:
            ones = []
            # separate current puzzle into ones, 'bdeg' -> 0b1011010 -> [0b10(b), 0b1000(d), 0b10000(e), 0b1000000(g)]
            for c in p:
                ones.append(1 << (ord(c) - orda))
            
            # generate all valid words for the current puzzle
            # equivalent to generate all subsets of ones[1:]
            # reuse code from [78. Subsets]
            valid = [ones[0]] # valid word must contains the first char of current puzzle
            for i in range(1,7): # bfs to generate all valid words
                valid.extend([ones[i] + v for v in valid])
            
            # for each valid word, check whether it's in mask
            novw = 0 # number of valid words for current puzzle
            for v in valid:
                if v in mask:
                    novw += mask[v]
            res.append(novw)
        return res
