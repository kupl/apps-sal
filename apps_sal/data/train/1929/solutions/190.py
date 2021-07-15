from collections import deque
class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.word = \"\"

class Trie:
    def __init__(self):
        self.root = Node(\"\")

    def add_word(self, word):
        def helper(next_idx, node):
            next_char = word[next_idx]
            if next_char not in node.children:
                node.children[next_char] = Node(next_char)
            node = node.children[next_char]
            if next_idx == len(word) - 1:
                node.word = word
            else:
                helper(next_idx+1, node)
        helper(0, self.root)

    def word_exists(self, word):
        def helper(next_idx, node):
            if node.word:
                return True
            if next_idx >= len(word):
                return False
                
            next_char = word[next_idx]
            if next_char not in node.children:
                return False
            node = node.children[next_char]
            return helper(next_idx+1, node)
            
        return helper(0, self.root)
        

class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.max_word_length = 0
        for word in words:
            self.trie.add_word(word[::-1])
            self.max_word_length = max(self.max_word_length, len(word))
        self.q = deque()

    def query(self, letter: str) -> bool:
        if len(self.q) == self.max_word_length:
            self.q.pop()
        self.q.appendleft(letter)
        return self.trie.word_exists(self.q)
    # [\"cde\"]
    # [\"c\" Node<d>, \"d\" None] e
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
