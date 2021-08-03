class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:

        counter = {}
        for word in words:
            mask = self.to_int(word)
            if mask not in counter:
                counter[mask] = 0
            counter[mask] += 1

        output = []
        for puzzle in puzzles:
            output.append(0)
            sub_strings = ['']
            mask = self.to_int(puzzle[1:])
            for c in puzzle[1:]:
                for sub_string in list(sub_strings):
                    sub_strings.append(sub_string + c)
            for sub_string in list(sub_strings):
                mask = self.to_int(puzzle[0] + sub_string)
                output[-1] += counter.get(mask, 0)

        return output

    def to_int(self, word):
        mask = 0
        for ch in word:
            mask |= 1 << (ord(ch) - 97)
        return mask
