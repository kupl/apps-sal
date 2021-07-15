class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        trie = {}
        result = [0 for _ in range(len(puzzles))]
        
        def dfs(puzzle, i, trie, hasFirst=False):        
            if \"*\" in trie and hasFirst:
                result[i] += trie[\"*\"]
                        
            for c in puzzle:
                if c in trie:
                    dfs(puzzle, i, trie[c], hasFirst or c == puzzle[0])
                            
        for w in words:
            curr = trie
            for c in sorted(set(w)):
                curr = curr.setdefault(c, {})
                    
                # curr = curr[c]
            
            if \"*\" in curr:
                curr[\"*\"] += 1
            else:
                curr[\"*\"] = 1
            
        print(curr)
            
        for i, p in enumerate(puzzles):
            dfs(p, i, trie)
            
        return result

