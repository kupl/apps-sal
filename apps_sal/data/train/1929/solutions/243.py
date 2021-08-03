class TrieNode:
    def __init__(self):
        self.next = {}
        self.is_word = False


class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for word in words:
            itr = self.root
            for c in word[::-1]:
                itr.next.setdefault(c, TrieNode())
                itr = itr.next[c]
            itr.is_word = True
        self.stream = deque()

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        curr = self.root
        for c in self.stream:
            if c in curr.__next__:
                curr = curr.next[c]
                if curr.is_word:
                    return True
            else:
                break
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
