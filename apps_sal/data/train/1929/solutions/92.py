class TrieNode:
    def __init__(self, eow):
        self.children = {}
        self.eow = eow

class Trie:
    def __init__(self):
        self.root = TrieNode(False)

    def add(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode(False)

            cur = cur.children[ch]

        cur.eow = True

class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.add(word)

        self.trie_curs = [self.trie.root]

    def query(self, letter: str) -> bool:
        trie_curs_new = [self.trie.root]
        hit = False
        for cur in self.trie_curs:
            if letter in cur.children:
                trie_curs_new.append(cur.children[letter])
                if not hit and cur.children[letter].eow:
                    hit = True

        self.trie_curs = trie_curs_new

        return hit
