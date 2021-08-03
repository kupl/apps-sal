class TrieNode:
    def __init__(self):
        self.dic = {}
        self.end = False
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for word in words:
            word = \"\".join(reversed(word))
            self.addword(word)
        self.stream = \"\"
            
    def addword(self, word):
        current = self.root
        for char in word:
            if char not in current.dic:
                current.dic[char] = TrieNode()
            current = current.dic[char]
        current.end = True
            
    def helper(self, current, stream):
        for i in range(len(stream)):
            if stream[i] not in current.dic: 
                if current.end:
                    return True
                else:
                    return False
            else:
                if current.end:
                    return True
            current = current.dic[stream[i]]
        return current.end
        
    def query(self, letter: str) -> bool:
        self.stream = letter + self.stream
        return self.helper(self.root, self.stream)
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
