class Trie:
    def __init__(self):
        self.wordEndsHere = False
        self.children = dict()
        
    def addWord(self, word):
        if not word:
            self.wordEndsHere = True
        else:
            if word[0] not in self.children:
                self.children[word[0]] = Trie()
            self.children[word[0]].addWord(word[1:])
    
    def findWord(self, word):
        if self.wordEndsHere:
            return True
        
        if not word:
            return self.wordEndsHere
        elif word[0] not in self.children:
            return False
        else:
            return self.children[word[0]].findWord(word[1:])

class StreamChecker:
    def __init__(self, words: List[str]):
        self.maxLength = 0
        self.letters = []
        self.trie = Trie()
        
        for w in words:
            self.trie.addWord(w[::-1])
            self.maxLength = max(self.maxLength, len(w))

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        sliceLength = min(len(self.letters), self.maxLength)
        target = ''.join(self.letters[(len(self.letters) - sliceLength):])[::-1]
        return self.trie.findWord(target)
