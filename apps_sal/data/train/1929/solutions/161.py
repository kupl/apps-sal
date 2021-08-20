class TrieNode:

    def __init__(self):
        self.child = {}
        self.isWord = False


class Tree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for w in word:
            if w not in cur.child:
                cur.child[w] = TrieNode()
            cur = cur.child[w]
        cur.isWord = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.tree = Tree()
        for word in words:
            self.tree.insert(word[::-1])
        self.letter = []

    def query(self, letter: str) -> bool:
        self.letter.append(letter)
        cur = self.tree.root
        i = len(self.letter) - 1
        while i >= 0:
            if cur.isWord:
                return True
            if self.letter[i] not in cur.child:
                return False
            cur = cur.child[self.letter[i]]
            i -= 1
        return cur.isWord
