from collections import defaultdict

class TrieNode:
    
    def __init__(self):
        self.children=defaultdict(TrieNode)
        self.isWord=False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root=TrieNode()
        self.mx_length=0
        for word in words:
            self.insert(word[::-1])
            self.mx_length=max(self.mx_length,len(word))
        
        self.buffer=''
        
        
    def insert(self,word):
        curr_node=self.root
        for ch in word:
            curr_node=curr_node.children[ch]
        curr_node.isWord=True
            
    def search(self,word):
        cur_node=self.root
        for ch in word:
            cur_node=cur_node.children.get(ch)
            if not cur_node:
                return False
            if cur_node.isWord:
                return True
        
        return False
        
        

    def query(self, letter: str) -> bool:
        self.buffer+=letter
        return self.search(self.buffer[::-1])


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

