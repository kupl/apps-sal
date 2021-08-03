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
        i = len(letters) - 1
        
        
        for l in letters[::-1]:
            
            if l in trie and '#' in trie[l]:
                print(\"HHHH\")
                return True
                break
            
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
        # # i = len(self.letters) - 1
        
        # node = self.trie_check.trie
        return self.trie_check.search(self.letters)
        
        # while i >= 0:
        #     if '#' in node:
        #         return True
        #     if self.letters[i] not in node:
        #         return False
        #     node = node[self.letters[i]]
        #     i -= 1
        # return True if '#' in node else False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
