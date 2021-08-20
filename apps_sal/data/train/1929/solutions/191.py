class TrieNode:

    def __init__(self):
        self.child = [None] * 26
        self.is_leaf = False


class StreamChecker:

    def __init__(self, words: List[str]):
        root = TrieNode()
        for word in words:
            l = len(word)
            node = root
            for i in range(l - 1, -1, -1):
                index = ord(word[i]) - 97
                if node.child[index] is None:
                    node.child[index] = TrieNode()
                node = node.child[index]
            node.is_leaf = True
        self.root = root
        self.queue = []

    def query(self, letter: str) -> bool:
        self.queue.append(letter)
        if len(self.queue) > 2000:
            self.queue.pop(0)
        index = len(self.queue) - 1
        node = self.root
        while index >= 0:
            current = ord(self.queue[index]) - 97
            node = node.child[current]
            if node is None:
                return False
            elif node.is_leaf:
                return True
            index -= 1
        return False
