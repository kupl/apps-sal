class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        
        word_profiles = {}
        letters = \"abcdefghijklmnopqrstuvwxyz\"
        for word in words:
            word_profile = 0
            for letter in word:
                word_profile |= 1<<letters.index(letter)
            if not word_profile in word_profiles:
                word_profiles[word_profile] = 0
            word_profiles[word_profile] += 1
        
        for puzzle in puzzles:
            puzzle_profile = 0
            for letter in puzzle:
                puzzle_profile |= 1<<letters.index(letter)
            
            first_letter = 1<<letters.index(puzzle[0])
            
            candidate = puzzle_profile
            cnt = 0
            while candidate > 0:
                if candidate in word_profiles and candidate&first_letter == first_letter:
                    cnt += word_profiles[candidate]
                candidate -= 1
                candidate &= puzzle_profile
            
            yield(cnt)
