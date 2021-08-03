class Trie:
    \"\"\"
    Implementation of a prefix tree.
    \"\"\"

    def __init__(self):
        self.root = {}

    def add_word(self, w: str) -> None:
        currNode = self.root
        for c in w:
            if c not in currNode:
                currNode[c] = {}

            currNode = currNode[c]

        currNode['#'] = True  # Mark the word end.


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for w in words:
            self.trie.add_word(w)

        self.startNodes = []

    def query(self, letter: str) -> bool:
        nextStartNodes = [
            node[letter] for node in self.startNodes + [self.trie.root]
            if letter in node]
        self.startNodes = nextStartNodes
        return any('#' in node for node in nextStartNodes)
