class TrieNode:
    def __init__(self, ch):
        self.val = ch
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode('')
    
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                curr.children[ch] = TrieNode(ch)
                curr = curr.children[ch]
        curr.is_word = True
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.string = ''

    def query(self, letter: str) -> bool:
        self.string += letter
        curr = self.trie.root
        for ch in self.string[::-1]:
            if ch in curr.children:
                curr = curr.children[ch]
                if curr.is_word:
                    return True
            else:
                return False
        return curr.is_word


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

