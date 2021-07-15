class Solution:
    def conv(self, c):
        return ord(c) - ord('a')
    
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        first_letters = {chr(c): set([]) for c in range(ord('a'), ord('z') + 1)} # maps chars to set of words containing the char
        word_masks = {} # maps bitmask of word to its index
        for i, w in enumerate(words):
            mask = 0
            for c in w:
                first_letters[c].add(i)
                mask = (1 << self.conv(c)) | mask
            if mask not in word_masks:
                word_masks[mask] = []
            word_masks[mask].append(i)
        puzzle_masks = []
        for p in puzzles:
            mask = 0
            for c in p:
                mask = (1 << self.conv(c)) | mask
            puzzle_masks.append(mask)
        
        answer = []
        for i, m in enumerate(puzzle_masks):
            s = m
            total = 0
            while s != 0:
                if s in word_masks:
                    for w in word_masks[s]:
                        if w in first_letters[puzzles[i][0]]:
                            total += 1
                s = (s - 1) & m
            answer.append(total)
        
        return answer
