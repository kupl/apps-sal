class TrieNode:
        
    def __init__(self):
        self.is_word = False
        self.children = dict()

class StreamChecker:
    \"\"\"Seems super slow?...\"\"\"

    def __init__(self, words: List[str]):
        self._root = TrieNode()
        self._valid_nodes = list()
        for word in words:
            self._insert(word)
        
            
    def _insert(self, word: str):
        node = self._root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.is_word = True

    def query(self, letter: str) -> bool:
        # Shallow copy should be enough
        # node = copy.copy(self._root)
        node = self._root
        self._valid_nodes.append(node)
        next_valid_nodes = list()
        found = False
        for node in self._valid_nodes:
            if letter in node.children:
                node = node.children[letter]
                next_valid_nodes.append(node)
                if node.is_word:
                    found = True
        self._valid_nodes = next_valid_nodes
        return found
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
