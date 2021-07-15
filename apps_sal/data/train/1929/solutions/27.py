class Trie:
    def __init__(self):
        self.children = defaultdict(list)
        self.end_of_word = False

        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Trie()
        self.nodes = []
        for word in words:
            self.addWord(word)

        
    def addWord(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = Trie()
            node = node.children[w]
        node.end_of_word = True

        
    def query(self, letter: str) -> bool:
        self.nodes.append(self.root)
        temp = False
        new_nodes = []
        
        for node in self.nodes:
            if letter in node.children:
                node = node.children[letter]
                if node.end_of_word:
                    temp = True
                new_nodes.append(node)
        self.nodes = new_nodes
        return temp
        
        

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

