
class Trie(object):
    class Node(object):
        def __init__(self, end=False):
            self.children = {}
            self.end = end

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.root = self.Node()

    def insert(self, word):
        \"\"\"
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        \"\"\"
        current_node = self.root
        prev_node = current_node
        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = self.Node()
            prev_node = current_node
            current_node = current_node.children[letter]
        prev_node.children[letter].end = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for w in words:
            self.trie.insert(w)
        self.current_nodes = [self.trie.root]

    def query(self, letter: str) -> bool:
        self.current_nodes = [cn.children[letter] for cn in self.current_nodes if letter in cn.children]
        if self.trie.root not in self.current_nodes:
            self.current_nodes.append(self.trie.root)
        end = any([cn.end for cn in self.current_nodes])
        return end

    
