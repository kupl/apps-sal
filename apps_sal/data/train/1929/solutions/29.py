class TrieNode:
    def __init__(self, value, leaf=False, children=None):
        self.children = children or {}
        self.value = value
        self.leaf = leaf


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode(value=None)
        self.pointers = []
        for word in words:
            node = self.root
            for c in word:
                if c not in node.children:
                    c_node = TrieNode(c)
                    node.children[c] = c_node
                node = node.children[c]
            node.leaf = True

    def query(self, letter: str) -> bool:
        result = False
        revised_pointers = []
        self.pointers.append(self.root)
        for pointer in self.pointers:
            if letter in pointer.children:
                node = pointer.children[letter]
                if node.leaf:
                    result |= True
                revised_pointers.append(node)
        self.pointers = revised_pointers
        return result
