class Trie:

    def __init__(self):
            \"\"\"
            Initialize your data structure here.
            \"\"\"
            self.trie = {}


    def insert(self, word: str) -> None:
        \"\"\"
        Inserts a word into the trie.
        \"\"\"
        trie = self.trie
        for w in word:
            if w not in trie:
                trie[w] = {}
            trie = trie[w]
        trie['#'] = '#'
    
    def search(self, letters):
        
        trie = self.trie
        letters = letters[::-1]
        
        for l in letters:
            
            if '#' in trie:
                return True
            
            if l not in trie:
                return False
            
            trie = trie[l]
            
        if '#' in trie:
            return True
        else:
            return False
            

class StreamChecker:

    def __init__(self, words: List[str]):
        self.letters = []
        
        self.trie_check = Trie()
        for w in words:
            self.trie_check.insert(w[::-1])
        

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        return self.trie_check.search(self.letters)
        
       


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
