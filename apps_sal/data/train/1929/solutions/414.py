class TrieNode:
    
    def __init__(self):
        
        self.nodes = {}
        self.is_word = False
        

class StreamChecker:

    def __init__(self, words: List[str]):
        self.prefix = \"\"
        self.trienode = TrieNode()

        for word in words:
            node = self.trienode
            for c in word[::-1]:
                if c not in node.nodes:
                    node.nodes[c] = TrieNode()
                node = node.nodes[c]
            node.is_word = True

    def query(self, letter: str) -> bool:
        self.prefix += letter

        node = self.trienode
        for c in self.prefix[::-1]:
            if c not in node.nodes:
                break
            node = node.nodes[c]
            if node.is_word:
                return True
        
        return False

