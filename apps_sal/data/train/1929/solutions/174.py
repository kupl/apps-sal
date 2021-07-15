class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class StreamChecker:
    
    def __init__(self, words: List[str]):
        self.cache = Node()
        self.stream = []
        for word in words:
            root = self.cache
            for i in range(len(word) - 1, -1, -1):
                if word[i] in root.children:
                    root = root.children.get(word[i])
                else:
                    root.children[word[i]] = Node()
                    root = root.children.get(word[i])
            root.is_word = True

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        root = self.cache
        for i in range(len(self.stream) - 1, -1, -1):
            if self.stream[i] not in root.children:
                return False
            
            root = root.children.get(self.stream[i])
            if root.is_word:
                return True
            
        return False
        
        
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

