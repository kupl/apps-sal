class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.isWord = False
        
class StreamChecker:
    def __init__(self, words: List[str]):
        self.trieRoot = TrieNode()
        self.stream = \"\"
        
        for word in words:
            self.addWord(word[::-1])
    
    def addWord(self, word: str) -> None:
        \"\"\"
        Adds a word into the data structure.
        \"\"\"
        current_node = self.trieRoot
        for char in word:
            current_node = current_node.nodes[char]
        
        current_node.isWord = True
    
    def query(self, letter: str) -> bool:
        self.stream += letter
        word = self.stream[::-1]
        curr = self.trieRoot
        
        for char in word:
            if char not in curr.nodes:
                return False
            
            curr = curr.nodes[char]
            if curr.isWord:
                return True
            
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
