from collections import deque


class Node:

    def __init__(self):
        self.children = dict()
        self.isEnd = False
        self.word = \"\"


class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word):
        current = self.root

        for i in range(len(word)):
            if current.children.get(word[i], None) is None:
                current.children[word[i]] = Node()
            current = current.children[word[i]]
        current.isEnd = True
        current.word = word

    # def query(self, letter):
        

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.q = deque()
        for word in words:
            self.trie.insert(word[::-1])

        

    def query(self, letter: str) -> bool:
        self.q.appendleft(letter)
        current = self.trie.root

        for c in self.q:
            if c in current.children:
                current = current.children[c]
                if current.isEnd:
                    return True
            else:
                return False
        return False


        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
