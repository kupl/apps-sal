class Trie:

    def __init__(self):
        self.root = {}
        self.curr = self.root

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['.'] = True

    def search(self, char):
        node = self.curr
        if char in node:
            node = node[char]
            self.curr = node
            return '.' in node
        else:
            self.curr = self.root
            return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = deque()
        self.trie = Trie()
        for w in words:
            self.trie.add(w[::-1])

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node = self.trie.root
        for char in self.stream:
            if char in node:
                node = node[char]
                if '.' in node:
                    return True
            else:
                break
        return False


'\n[[["ab","ba","aaab","abab","baa"]],\n["a"],["a"],["a"],["a"],["a"],["b"],["a"],\n  F     F     F     F     F     T     T\n'
