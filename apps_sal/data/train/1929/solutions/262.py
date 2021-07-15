class TrieNode:
    def __init__(self):
        self.isWord=False
        self.child = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add_word(self, word):
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.child:
                cur.child[word[i]]=TrieNode()
            cur =cur.child[word[i]]
        cur.isWord=True
    
    def search_word(self, word):
        cur=self.root
        for i in range(len(word)):
            if word[i] not in cur.child:
                return False
            else:
                cur=cur.child[word[i]]
        return cur.isWord
             
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie=Trie()
        self.max_length = max(len(word) for word in words)
        self.letters =collections.deque()
        for word in words:
            self.trie.add_word(word[::-1])

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        if len(self.letters)>self.max_length:
            self.letters.popleft()
        
        t = list(self.letters)[::-1]
        cur = self.trie.root
        for letter in t:
            if letter not in cur.child:
                return False
            cur=cur.child[letter]
            if cur.isWord:
                return True
        return False
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

