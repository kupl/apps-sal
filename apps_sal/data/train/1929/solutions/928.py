class Trie:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.isEnd = False


class TireTree:
    def __init__(self):
        self.root = Trie('')

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie(c)
                cur = cur.children[c]
            else:
                cur = cur.children[c]
        cur.isEnd = True

    def search(self, word, cur):
        for c in word:
            if c not in cur.children:
                return False

            cur = cur[c]
        return cur.isEnd


class StreamChecker:

    def __init__(self, words: List[str]):
        self.tree = TireTree()
        for word in words:
            self.tree.insert(word)
        self.root = self.tree.root
        self.paths = [self.root]

    def query(self, letter: str) -> bool:
        nextpaths = [self.root]
        flag = False
        for p in self.paths:
            if letter in p.children:
                node = p.children[letter]
                nextpaths.append(node)

                if node.isEnd:
                    flag = True

        self.paths = nextpaths
        return flag
