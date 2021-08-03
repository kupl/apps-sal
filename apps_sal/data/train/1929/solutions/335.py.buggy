class Trie:
    def __init__(self, is_leaf):
        \"\"\"
        { element : {val : 1, is_end: False}]}

       \"\"\"
        self.is_leaf = is_leaf
        self.child = {}


class StreamChecker:

    def __init__(self, words: List[str]):
        # print(\"its here\")
        self.trie = {}
        self.max_length = 0
        self.word = \"\"
        for word in words:
            self.max_length = len(word) if len(word) > self.max_length else self.max_length
            self.insert_word(word)

    def query(self, letter: str) -> bool:
        self.word += letter
        self.word = self.word[-self.max_length:] if len(self.word) > self.max_length else self.word
        ans = self.search_word()
        return ans

    def insert_word(self, word):
        head = self.trie
        for i in range(len(word) - 1, -1, -1):
            if word[i] not in head:
                t = Trie(True) if i == 0 else Trie(False)
                head[word[i]] = t
                head = t.child
            else:
                node = head.get(word[i])
                if i == 0:
                    node.is_leaf = True
                head = node.child
                
                # print(head)

                
    def search_word(self):
        # print(\"searching \", self.word)
        head = self.trie
        # print(head)
        node = None
        for i in range(len(self.word) - 1, -1, -1):
            # print(\"letter \", self.word[i])
            if self.word[i] in head:
                node = head.get(self.word[i])
                head = node.child
                if node.is_leaf:
                    return True
            else:
                return False
        return node.is_leaf

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
