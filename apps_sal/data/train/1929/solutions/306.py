class TrieNode:
    def __init__(self, char):
        self.node = char
        self.children = {}
        self.end_word = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = TrieNode('*')
        for word in words:
            curr_node = self.trie
            for char in word[::-1]:
                node = curr_node.children.get(char, TrieNode(char))
                curr_node.children[char] = node
                curr_node = node
            curr_node.end_word = True
        self.queried = ''
    
    def exists(self, word):
        #dc
        curr_node = self.trie
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
            if curr_node.end_word:
                return True
        if curr_node.end_word:
            return True
        return False

    def query(self, letter: str) -> bool:
        root = self.trie
        self.queried = letter + self.queried
        if self.exists(self.queried):
            return True
        return False
        
'''
 * (d->c->e, f, l->k)


[a,b,c,]


1. checking the actual problem
2. checking the trie
'''        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

