class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.isWord = False
        
class StreamChecker:
    def __init__(self, words: List[str]):
        self.trieRoot = TrieNode()
        self.stream = \"\"
        self.words = {}
        self.minWordLen = float(\"inf\")
        
        for word in words:
            self.addWord(word[::-1])
            if len(word) < self.minWordLen:
                self.minWordLen = len(word)
        
    def addWord(self, word: str) -> None:
        \"\"\"
        Adds a word into the data structure.
        \"\"\"
        current_node = self.trieRoot
        #print(\"Inserting =\", word)
        for char in word:
            #print(\"Char =\", char)
            current_node = current_node.nodes[char]
        
        current_node.isWord = True
        self.words[word] = True
        #print(self.words)
    
    def query(self, letter: str) -> bool:
        self.stream += letter
        word = self.stream[::-1]
        
        curr = self.trieRoot
        
        for char in word:
            #print(\"One by one:\", char)
            if char not in curr.nodes:
                #print(\"returning False\")
                return False
            curr = curr.nodes[char]
            if curr.isWord:
                return True

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
