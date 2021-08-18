class Node:
    def __init__(self):
        self.children = {}
        self.stop = False


class Trie:
    def __init__(self):
        self.word = Node()

    def insert(self, word):
        word = word[::-1]
        curr = self.word
        for l in word:
            node = curr.children.get(l, Node())
            curr.children[l] = node
            curr = node
        curr.stop = True

    def search(self, word):
        curr = self.word

        for l in word:
            node = curr.children.get(l, None)

            if not node:
                return False
            elif node.stop:
                return True
            curr = node
        return curr.stop


class StreamChecker:

    def __init__(self, words: List[str]):
        self.t = Trie()
        for word in words:
            self.t.insert(word)
        self.pointer = ''

    def query(self, letter: str) -> bool:
        self.pointer += letter

        return self.t.search(self.pointer[::-1])
