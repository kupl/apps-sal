class Trie:
    def __init__(self):
        self.children = defaultdict(bool)
        # self.children = {}

    def insert(self, word):
        if word == '':
            self.children['@'] = True
        else:
            child = self.children[word[0]]
            if child:
                child.insert(word[1:])
            else:
                newChild = Trie()
                newChild.insert(word[1:])
                self.children[word[0]] = newChild


class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = Trie()
        for word in words:
            self.root.insert(word)
        self.pointers = []

    def query(self, letter: str) -> bool:
        newPointers = []
        retFlag = False
        self.pointers.append(self.root)
        for p in self.pointers:
            newP = p.children[letter]
            if newP:
                newPointers.append(newP)
                if '@' in newP.children:
                    retFlag = True
        self.pointers = newPointers
        return retFlag
