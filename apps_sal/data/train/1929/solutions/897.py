class Trie:
    def __init__(self):
        self.children = defaultdict(lambda: False)
    def insert(self,word):
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
        # print(self.pointers)
        retFlag = False
        if letter in self.root.children:
            newPointers.append(self.root.children[letter])
            if '@' in self.root.children[letter].children:
                retFlag = True
        for p in self.pointers:
            newP = p.children[letter]
            if newP:
                newPointers.append(newP)
                if '@' in newP.children:
                    retFlag = True
        self.pointers = newPointers
        return retFlag


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

