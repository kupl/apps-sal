from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_word = False


class StreamChecker:
    def __init__(self, words: List[str]):
        self.stream = ''
        self.trie = Trie()

        for word in words:
            curr = self.trie
            for ch in word[::-1]:
                curr = curr.children[ch]
            curr.is_word = True

    def query(self, letter: str) -> bool:
        self.stream += letter
        curr = self.trie

        for ch in self.stream[::-1]:
            if ch not in curr.children:
                return False

            curr = curr.children[ch]

            if curr.is_word:
                return True

        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
