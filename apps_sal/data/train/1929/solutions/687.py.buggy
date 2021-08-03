class StreamChecker:

    def __init__(self, words: List[str]):
        self.queryStr = \"\"
        self.trie = dict()
        for word in words:
            currNode = self.trie
            for letter in word[::-1]:
                if letter not in currNode:
                    currNode[letter] = {}
                currNode = currNode[letter]
            currNode['#'] = {}             

    def query(self, letter: str) -> bool:
        self.queryStr += letter
        currNode = self.trie
        for l in self.queryStr[::-1]:
            if l not in currNode:
                return False
            
            currNode = currNode[l]
                
            if '#' in currNode:
                return True

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
