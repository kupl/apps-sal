class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Node(\"thisisroot\")
        
        for word in words:
            node = self.root
            for char in word[::-1]:
                if not char in node.children:
                    node.children[char] = Node(char)
                node = node.children[char]
            node.isWord = True
            
        self.prefix = \"\"
            
    def query(self, letter: str) -> bool:
        self.prefix += letter
        node = self.root
        for char in self.prefix[::-1]:
            if char not in node.children: break
            tmp = node.children[char]
            if tmp.isWord: return True
            node = tmp
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
