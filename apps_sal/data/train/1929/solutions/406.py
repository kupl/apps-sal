from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.dict = defaultdict(TrieNode)
        self.is_word = False

class StreamChecker:
    def __init__(self, words: List[str]):
        # Build a trie with the words in reverse order\t\t
        
        # for user query record, init as empty string
        self.prefix = ''
        
        # for root node of trie, init as empty Trie
        self.trie = TrieNode()
        
        for word in words:
            curr_node = self.trie
            
\t\t\t# make word in reverse order
            word = word[::-1]
            
            for char in word:                
                curr_node = curr_node.dict[ char ]
            
\t\t\t# mark this trie path as a valid word
            curr_node.is_word = True

    def query(self, letter: str) -> bool:
        self.prefix += letter
        
        curr_node = self.trie
        for char in self.prefix[::-1]:
            if char not in curr_node.dict:
                # word not in trie
                break
            curr_node = curr_node.dict[char] # get into next node
            if curr_node.is_word:
                # found word
                return True
        # No match
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
