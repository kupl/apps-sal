class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def binarize(word):
            ans = 0
            for c in word:
                ans |= (1 << (ord(c) - ord(\"a\")))
            ans = bin(ans)[2:]
            return \"0\" * (26 - len(ans)) + ans
        
        words = [binarize(word) for word in words if len(set(word)) < 8]
        trie = {}
        for i, word in enumerate(words):
            temp = trie
            for c in word:
                if c not in temp:
                    temp[c] = {}
                temp = temp[c]
            if \"*\" not in temp:
                temp[\"*\"] = []
            temp[\"*\"] += [i]
            
        puzzles = [(puzzle[0], binarize(puzzle)) for puzzle in puzzles]
        ans = []
        for c, puzzle in puzzles:
            tries = [trie]
            for b in puzzle:
                new_tries = []
                
                for temp in tries:
                    if \"0\" in temp:
                        new_tries += [temp[\"0\"]]
                    if b == \"1\" and \"1\" in temp:
                        new_tries += [temp[\"1\"]]
                        
                tries = new_tries
                
            count = 0
            for temp in tries:
                for i in temp[\"*\"]:
                    if words[i][25 - ord(c) + ord(\"a\")] == \"1\":
                        count += 1
            ans += [count]
            
        return ans
