class TrieNode:
    def __init__(self):
        self.is_word = False
        self.chars = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.prev_nodes = []

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.chars:
                curr.chars[c] = TrieNode()
            curr = curr.chars[c]
        curr.is_word = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()

        for word in words:
            self.trie.addWord(word)

    def query(self, letter: str) -> bool:
        curr_nodes = []
        for prev_node in self.trie.prev_nodes:
            if letter in prev_node.chars:
                curr_nodes.append(prev_node.chars[letter])
        if letter in self.trie.root.chars:
            curr_nodes.append(self.trie.root.chars[letter])
        self.trie.prev_nodes = curr_nodes
        found_letter = False
        for node in curr_nodes:
            if node.is_word:
                found_letter = True
        return found_letter


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
