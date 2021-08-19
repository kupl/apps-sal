class Node:

    def __init__(self, char):
        self.char = char
        self.nxts = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = Node('')

    def _add(self, node, word):
        if word == '':
            node.end = True
            return
        if word[0] not in node.nxts:
            node.nxts[word[0]] = Node(word[0])
        self._add(node.nxts[word[0]], word[1:])

    def add(self, word):
        self._add(self.root, word)

    def _search(self, node, word):
        if node.end is True:
            return True
        if word == '':
            return node.end is True
        if word[0] in node.nxts:
            return self._search(node.nxts[word[0]], word[1:])
        return False

    def search(self, word):
        return self._search(self.root, word)


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for w in words:
            self.trie.add(w[::-1])
        self.sofar = ''

    def query(self, letter: str) -> bool:
        self.sofar = letter + self.sofar
        return self.trie.search(self.sofar)
