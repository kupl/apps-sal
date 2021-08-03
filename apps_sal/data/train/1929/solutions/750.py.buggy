from collections import defaultdict

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.previous = []
        for word in words:
            path = self.trie
            for letter in word:
                if letter not in path:
                    path[letter] = {}
                    
                path = path[letter]
            path[\"END\"] = {}

    def query(self, letter: str) -> bool:
        found = False
        
        next = []
        for previous in self.previous:
            if letter in previous:
                if \"END\" in previous[letter]:
                    found = True
                #print(f\"test: {letter}, {previous[letter]}\")
                next.append(previous[letter])
        self.previous = next
        
        if letter in self.trie:
            if \"END\" in self.trie[letter]:
                found = True
            self.previous.append(self.trie[letter])
        
        #print(f\"{letter}: {found}, {self.previous}\")
        return found
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
