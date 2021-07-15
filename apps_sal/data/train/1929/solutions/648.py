class TrieNode:
    
    def __init__(self):
        
        self.children = {}
        self.isWord = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = TrieNode()
        self.prefix = \"\"
        ######################### SAVE IN REVERSED ORDER !!!!!!!!!!!!!!!!!!!!
        for word in words:
            cur = self.trie
            for char in word[::-1]:
                if not cur.children.get(char):
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.isWord = True
            
    def query(self, letter: str) -> bool:
        self.prefix += letter
        cur = self.trie
        for char in self.prefix[::-1]:
            if not cur.children.get(char):
                return False
            cur = cur.children[char]
            if cur.isWord:
                return True
            
