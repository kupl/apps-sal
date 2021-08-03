class Node:
    def __init__(self):
        self.list = [None] * 26
        self.period = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        curr = self.root
        for i in range(len(word) - 1, -1, -1):
            letter = word[i]
            asc = ord(letter) - ord('a')
            if not curr.list[asc]:
                curr.list[asc] = Node()
            curr = curr.list[asc]
        curr.period = True

    def query(self, word):
        curr = self.root
        for i in range(len(word) - 1, -1, -1):
            c = word[i]
            asc = ord(c) - ord('a')
            if not curr.list[asc]:
                return False
            curr = curr.list[asc]
            if curr.period == True:
                return True
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.query_list = []
        self.words = words

        for word in words:
            self.trie.add(word)

    def query(self, letter: str) -> bool:
        self.update_queries(letter)
        return self.trie.query(self.query_list)

    def update_queries(self, letter):
        self.query_list.append(letter)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
