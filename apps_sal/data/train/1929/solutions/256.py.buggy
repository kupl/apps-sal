
class Node:
    def __init__(self):
        self.word = False 
        self.children = {}

class StreamChecker:

    def __init__(self, words: List[str]):
        
        self.words = words
        self.word = \"\"
        self.head = Node()
        for word in words:
            word = word[::-1]
            ptr = self.head
            for cha in word:
                if cha not in ptr.children:
                    ptr.children[cha] = Node()
                ptr = ptr.children[cha]
            ptr.word = True 
                    

    def query(self, letter: str) -> bool:
        self.word+=letter 
        
        length = len(self.word)
        ptr = self.head 
        for i in range(length-1, -1, -1):
            if self.word[i] not in ptr.children:
                return False 
            ptr = ptr.children[self.word[i]]
            if ptr.word:
                return True 
        return False 
        
        
            
            
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
