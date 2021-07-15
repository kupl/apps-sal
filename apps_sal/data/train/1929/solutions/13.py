class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for ele in words:
            self.add(ele)
        self.stack = [self.root]
            
    def add(self,ele):
        current = self.root
        for char in ele:
            current = current.children[char]
        current.last = True
        
    def query(self, letter: str) -> bool:
        flag = False
        new_stack = [self.root]
        for ele in self.stack:
            if letter in ele.children:
                new_stack.append(ele.children[letter])
                if ele.children[letter].last:
                    flag = True
        self.stack = new_stack
        if flag:
            return True
        return False

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.last = False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

