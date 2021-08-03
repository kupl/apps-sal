class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.isWord = False
class Trie:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.root = Node()

    def insert(self, word: str) -> None:
        \"\"\"
        Inserts a word into the trie.
        \"\"\"
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.isWord = True

    def search(self, word: str) -> bool:
        \"\"\"
        Returns if the word is in the trie.
        \"\"\"
        node = self.root
        for ch in word:
            if ch not in node.children:
                break
            node = node.children.get(ch)
            if node.isWord:
                return True
        return False
class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = words
        self.chars = ''
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.chars += letter
        return self.trie.search(self.chars[::-1])

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
