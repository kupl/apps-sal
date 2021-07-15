class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.add(word[::-1])
        self.sb = []

    def query(self, letter: str) -> bool:
        self.sb.append(letter)
        i = len(self.sb)-1
        node = self.trie
        while i >= 0:
            if node.is_word:
                return True
            if self.sb[i] in node.words:
                node = node.words[self.sb[i]]
                i -= 1
            else:
                return False
        return node.is_word    
            

class Trie:
    def __init__(self):
        self.is_word = False
        self.prefix = ''
        self.words = {}
    
    def add(self, word):
        if not word:
            self.is_word = True
            return
        if word[0] in self.words:
            self.words[word[0]].add(word[1:])
        else:
            n = Trie()
            n.prefix = self.prefix + word[0]
            self.words[word[0]] = n
            self.words[word[0]].add(word[1:])



# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

