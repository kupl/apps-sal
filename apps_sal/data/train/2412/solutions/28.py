class Solution:
    def removeDuplicates(self, S: str) -> str:
        letters = list(S) + ['#']
        while True:
            nLetters = []
            i = 0
            while i < len(letters) - 1:
                if letters[i] != letters[i + 1]:
                    nLetters.append(letters[i])
                    i += 1
                else:
                    i += 2

            if len(nLetters) + 1 == len(letters): 
                break
            letters = nLetters + ['#']
        return ''.join(letters[:-1])
                
        

