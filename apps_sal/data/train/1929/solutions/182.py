class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.isEnd = False
        

class StreamChecker:
    def add_word(self, word):
        word = word[::-1]
        i = 0
        curr = self.root
        while i < len(word):
            if word[i] in curr.children:
                curr = curr.children[word[i]]
                if i == len(word)-1:
                    curr.isEnd = True
                i += 1
            else:
                break
        while i < len(word):
            curr.children[word[i]] = Node(word[i])
            curr = curr.children[word[i]]
            if i == len(word)-1:
                curr.isEnd = True
            i += 1

    def __init__(self, words: List[str]):
        self.root = Node()
        self.stream = \"\"
        for w in words:
            self.add_word(w)

    def query(self, letter: str) -> bool:
        self.stream  = letter + self.stream
        i = 0
        curr = self.root
        while i < len(self.stream):
            if self.stream[i] in curr.children:
                curr = curr.children[self.stream[i]]
                if curr.isEnd:
                    return True
            else:
                return False
            i += 1
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
