class Node:
    def __init__(self, val='.'):
        self.val = val
        self.children = {}
        self.is_word = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = self.__init_trie(words)
        self.q = []

    def query(self, letter: str) -> bool:
        self.q.append(self.root)
        new_q = []
        found = False
        for node in self.q:
            if letter in node.children:
                child_node = node.children[letter]
                new_q.append(child_node)
                if child_node.is_word:
                    found = True
        self.q = new_q
        return found

    def __init_trie(self, words):
        root = Node()
        for word in words:
            cur = root
            for i, ch in enumerate(word):
                if ch not in cur.children:
                    cur.children[ch] = Node(ch)
                cur = cur.children[ch]
            cur.is_word = True
        return root
