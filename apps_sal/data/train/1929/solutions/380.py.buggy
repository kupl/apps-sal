class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.end = False

class StreamChecker:

    def char_to_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        n = len(word)
        ptr = self.root
        for lvl in range(len(word)-1,-1,-1):
            i = self.char_to_index(word[lvl])
            if ptr and not ptr.children[i]:
                ptr.children[i] = TrieNode()

            ptr = ptr.children[i]

        ptr.end = True

    def __init__(self, words):
        self.root = TrieNode()
        self.pe = \"\"

        for word in words:
            self.insert(word)

    def query(self, letter):
        self.pe = letter + self.pe
        n = len(self.pe)
        node = self.root
        for lvl in range(n):
            i = self.char_to_index(self.pe[lvl])
            if node.children[i]:
                if node.children[i].end:
                    return True
            else:
                return False
            
            node = node.children[i]
            if not node:
                return False
       


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

