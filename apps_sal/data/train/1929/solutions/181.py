class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Trie:
    def __init__(self, corpus):
        self.root = TrieNode()
        for word in corpus:
            self.add(word)
        
    def add(self, word):
        x = self.root
        for w in word:
            if w not in x.children:
                x.children[w] = TrieNode()
            x = x.children[w]
        x.isEnd = True


class StreamChecker:

    def __init__(self, words: List[str]):
        words = [x[::-1] for x in words]
        self.trie = Trie(words)
        self.stream = deque()
        
    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        
        node = self.trie.root
        for w in self.stream:
            if node.isEnd:
                return True
            elif w not in node.children:
                return False
            else:
                node = node.children[w]
        return node.isEnd


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

