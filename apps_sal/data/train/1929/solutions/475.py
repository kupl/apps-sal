class StreamChecker:

    def __init__(self, words: List[str]):
        self.s = ''
        self.trie = Trie()
        for wrd in words:
            self.trie.insert(wrd[::-1])

    def query(self, letter: str) -> bool:
        self.s += letter
        node = self.trie.root
        for ch in self.s[::-1]:
            if ch in node.childs:
                node = node.childs[ch]
                if node.isWord:
                    return True
            else:
                break
        return False


class TrieNode:
    def __init__(self):
        self.childs = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        r = self.root
        for ch in word:
            r = r.childs.setdefault(ch, TrieNode())
        r.isWord = True
