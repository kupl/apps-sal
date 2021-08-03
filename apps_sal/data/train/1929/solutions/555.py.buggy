class TrieNode:
    def __init__(self):
        self.child={}
        self.isLeaf=False

class Trie():
    def __init__(self):
        self.root=TrieNode()
    
    def add(self,s):
        curr=self.root
        for ch in s:
            if ch not in curr.child:
                curr.child[ch]=TrieNode()
            curr=curr.child[ch]
        curr.isLeaf=True
        
    def print(self):
        curr=self.root
        
        def get(node,s):
            if node.isLeaf:
                print(\"got:\",s)
            for ch in node.child:
                get(node.child[ch],s+ch)
        get(curr,\"\")

class StreamChecker:

    def __init__(self, words: List[str]):
        self.t=Trie()
        self.q_word=''
        for word in words:
            self.t.add(word[::-1])
        #self.t.print()

    def query(self, letter: str) -> bool:
        self.q_word+=letter
        
        def find(node,s):
            for ch in s:
                if node.isLeaf:
                    return True
                if ch not in node.child:
                    return False
                node=node.child[ch]
            return node.isLeaf
            
        return find(self.t.root,self.q_word[::-1])


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
