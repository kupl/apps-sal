class TrieNode:

    def __init__(self) -> None:
        self.children = {}
        self.isWord = False


class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.isWord = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.queries = []
        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.queries.append(letter)
        idx = len(self.queries) - 1
        current = self.trie.root
        while idx >= 0:
            letter = self.queries[idx]
            if letter not in current.children:
                return False
            current = current.children[letter]
            if current.isWord:
                return True
            idx -= 1
        return False
