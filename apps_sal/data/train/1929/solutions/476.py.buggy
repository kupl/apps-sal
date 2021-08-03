class TrieNode:
    
    def __init__(self):
        
        self.nodes = {}
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word: str):
        root = self.root
        for c in word:
            root = root.nodes.setdefault(c, TrieNode())
        root.is_word = True

    def contains_substr(self, word: str):
        # Returns True if any beginning of word is contained in trie.
        root = self.root
        for c in word:
            if c not in root.nodes:
                break
            root = root.nodes[c]
            if root.is_word:
                return True
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.prefix = \"\"
        self.trie = Trie()

        for word in words:
            self.trie.insert_word(word[::-1])

    def query(self, letter: str) -> bool:
        self.prefix += letter
        return self.trie.contains_substr(self.prefix[::-1])
