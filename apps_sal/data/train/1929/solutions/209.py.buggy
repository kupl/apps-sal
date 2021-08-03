class TreeNode:
    def __init__(self):
        self.children = {}
        self.value = None
    def insert(self, string):
        root = self
        for char in string:
            if char not in root.children:
                root.children[char] = TreeNode()
            root = root.children[char]
        root.value = string
    def find(self, string):
        root = self
        for char in string:
            if char in root.children:
                root = root.children[char]
            else:
                return None
        return root.value
                 
class StreamChecker:
    def __init__(self, words):
        self.root = TreeNode()
        self.characters = \"\"
        for word in words:
            self.root.insert(word[::-1])
    def query(self, letter: str) -> bool:
        self.characters = letter + self.characters
        node = self.root
        for char in self.characters:
            if char in node.children:
                node = node.children[char]
                if node.value:
                    return True
            else:
                return False


