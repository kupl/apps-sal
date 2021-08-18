class Trie:

    def __init__(self):
        self.dict = {}
        self.leaf = False

    def addWord(self, word):
        curTrie = self
        for ch in word:
            if ch not in curTrie.dict:
                curTrie.dict[ch] = Trie()
            curTrie = curTrie.dict[ch]
        curTrie.leaf = True

    def search(self, query):
        curTrie = self
        for ch in query:
            if ch in curTrie.dict:
                curTrie = curTrie.dict[ch]
                if curTrie.leaf == True:
                    return True
            else:
                return False
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.queryStr = ''
        for word in words:
            self.trie.addWord(word[::-1])

    def query(self, letter: str) -> bool:
        self.queryStr += letter
        curTrie = self.trie
        return curTrie.search(self.queryStr[::-1])
