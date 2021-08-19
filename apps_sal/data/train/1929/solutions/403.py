class TrieNode:

    def __init__(self):
        self.dict = collections.defaultdict(TrieNode)
        self.isWord = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = ''

        self.root = TrieNode()
        for word in words:
            curr = self.root

            for char in word[::-1]:
                curr = curr.dict[char]

            curr.isWord = True

    def query(self, letter: str) -> bool:
        self.stream += letter
        curr = self.root
        for char in self.stream[::-1]:
            if char not in curr.dict:
                return False

            curr = curr.dict[char]
            if curr.isWord:
                return True


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
