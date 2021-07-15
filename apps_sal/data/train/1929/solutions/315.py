class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False
    

class StreamChecker:

    def __init__(self, words: List[str]):
        self.s = []
        self.root = TrieNode()
        for w in words:
            # self.insert(self.root,w)
            node = self.root
            for i in range(len(w)-1,-1,-1):
                idx = ord(w[i]) - ord('a')
                if not node.children[idx]:
                    node.children[idx] = TrieNode()
                node = node.children[idx]
            node.isEnd = True
        

    def query(self, letter: str) -> bool:
        self.s.append(letter)
        node = self.root
        for i in range(len(self.s)-1,-1,-1):
            idx = ord(self.s[i]) - ord('a')
            node = node.children[idx]  
            if node != None and node.isEnd:
                return True
            if node == None:
                return False
              
        # print(self.root.children)
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

