class Node:
    def __init__(self, val, is_word=False):
        self.val = val
        self.children = {}
        self.is_word = is_word

        
    def __repr__(self):
        return self.val


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Node(\"\")
        
        for word in words:
            node = self.root
            for letter in word:
                if letter not in node.children:
                    node.children[letter] = Node(letter)
                node = node.children[letter]
            node.is_word = True

        self.nodes = []
            
        
    def query(self, letter: str) -> bool:
        next_nodes = []
        for node in self.nodes:
            if letter in node.children:
                next_nodes.append(node.children[letter])
        self.nodes = next_nodes
        
        if letter in self.root.children:
            self.nodes.append(self.root.children[letter])

        for node in self.nodes:
            if node.is_word:
                return True
            
        return False
        

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
