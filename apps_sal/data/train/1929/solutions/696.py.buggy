import json

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.ptrs = []
        
        for word in words:
            curr = self.trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr[\".\"] = {}
    
    def query(self, letter: str) -> bool:
        res = False
        newPtrs = []
        
        if letter in self.trie:
            curr = self.trie[letter]
            newPtrs.append(curr)
            if \".\" in curr:
                res = True
        
        for ptr in self.ptrs:
            if letter in ptr:
                curr = ptr[letter]
                newPtrs.append(curr)
                if \".\" in curr:
                    res = True
        self.ptrs = newPtrs
        
        return res


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
