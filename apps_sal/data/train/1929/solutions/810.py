class Node:
    def __init__(self):
        self.next = {}
        self.isWord = False


class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = Node()
        self.ptr = self.root
        self.letters = []

        for w in words:
            node = self.root
            for c in w[::-1]:
                if c not in node.__next__:
                    node.next[c] = Node()
                node = node.next[c]
            node.isWord = True

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        idx, ptr = 0, self.root
        N = len(self.letters)

        for i in range(N - 1, -1, -1):
            c = self.letters[i]
            idx += 1
            if c not in ptr.__next__:
                return False
            ptr = ptr.next[c]
            if idx > 0 and ptr.isWord:
                return True
        return False
    
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

