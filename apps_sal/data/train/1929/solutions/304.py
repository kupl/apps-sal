class TrieNode:

    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.val = -1


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            current = current.children[char]
        current.val = 10

    def search(self, word):
        current = self.root
        for char in word:
            current = current.children.get(char)
            if not current:
                return False
        return current.val > 1

    def starts_with(self, word):
        current = self.root
        for char in word:
            current = current.children.get(char)
            if not current:
                return False
        return True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.letters = []
        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.letters += letter
        i = len(self.letters) - 1
        node = self.trie.root
        curr_word = ''
        for i in range(len(self.letters) - 1, -1, -1):
            curr_word += self.letters[i]
            has_sub_word = self.trie.starts_with(curr_word)
            if not has_sub_word:
                return False
            if has_sub_word and self.trie.search(curr_word):
                return True
        return False
