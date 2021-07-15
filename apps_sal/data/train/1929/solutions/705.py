class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        self.nodes = []
        for word in words:
            cur = self.root
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur['*'] = True
        
                

    def query(self, letter: str) -> bool: 
        self.nodes.append(self.root)
        newNodes = []
        ans = False
        for node in self.nodes:
            if letter in node:
                node = node[letter]
                if '*' in node:
                    ans = True
                newNodes.append(node)
        self.nodes = newNodes
        return ans
                
                


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

