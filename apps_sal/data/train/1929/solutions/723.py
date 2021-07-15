class Trie:
    def __init__(self, words):
        self.root = {}
        self.build(words)
    
    def build(self, words):
        for word in words:
            self.add_word(word)
            
    def add_word(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[\"$\"] = True

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie(words)
        self.prev_nodes = []

    def query(self, letter: str) -> bool:
        result = False
        new_nodes = []
        self.prev_nodes.append(self.trie.root)
        for node in self.prev_nodes:
            if letter in node:
                if \"$\" in node[letter]:
                    result = True
                new_nodes.append(node[letter])
        self.prev_nodes = new_nodes
        return result


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
