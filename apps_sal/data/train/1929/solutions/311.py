class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLeaf = False
        
    def add(self, word) -> None:
        if not word:
            return
        first = word[0]
        if first not in self.children:
            self.children[first] = TrieNode()
        if len(word) == 1:
            self.children[first].isLeaf = True
        self.children[first].add(word[1:])
        
    def search(self, word) -> bool:
        if not word:
            return self.isLeaf   
        first = word[0]
        if first not in self.children:
            return False
        return self.children[first].search(word[1:])
    

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trieRoot = TrieNode()
        for word in words:
            self.trieRoot.add(word[::-1])
        self.stream = []
        
    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        node = self.trieRoot
        for ch in reversed(self.stream):
            if ch in node.children:
                node = node.children[ch]
                if node.isLeaf:
                    return True
            else:
                break
                
        return False
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

