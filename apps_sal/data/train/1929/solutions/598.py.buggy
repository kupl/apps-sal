from collections import defaultdict


class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.end_of_word = False

        
class Trie:
    def __init__(self):
        self.root = TrieNode(\"*\")
        
    def insert(self, word):
        word = word[::-1]
        curr_node = self.root
        
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode(letter)
                
            curr_node = curr_node.children[letter]
        
        curr_node.end_of_word = True
        
    def word_exists(self, word):
        word = word[::-1]
        curr_node = self.root
        
        for letter in word:
            if letter not in curr_node.children:
                break
            
            curr_node = curr_node.children[letter]
            
            if curr_node.end_of_word:
                return True
        
        return False
            
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.string = \"\"
        self.trie = Trie()
        
        for word in words:
            self.trie.insert(word)
              

    def query(self, letter: str) -> bool:
        self.string += letter
        
        return self.trie.word_exists(self.string)
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
