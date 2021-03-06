class Trie:

    def __init__(self):
        self.dict = {}
        self.leaf = False

    def addWord(self, word):
        newTrie = Trie()
        if word[0] in self.dict:
            newTrie = self.dict[word[0]]
        else:
            self.dict[word[0]] = newTrie
        if len(word) == 1:
            newTrie.leaf = True
        else:
            newTrie.addWord(word[1:])


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.queryStr = ''
        for word in words:
            self.trie.addWord(word[::-1])

    def query(self, letter: str) -> bool:
        self.queryStr += letter
        curTrie = self.trie
        for ch in self.queryStr[::-1]:
            if ch in curTrie.dict:
                curTrie = curTrie.dict[ch]
                if curTrie.leaf == True:
                    return True
            else:
                return False
