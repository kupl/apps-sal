from collections import deque

class TrieNode:
    
    def __init__(self, word:str) -> None:
        self.children = {}
        self.exist = False
        
        if word is not None:
            self.add(word)
            
    def __repr__(self) -> str:
        return \"{\" + \", \".join([f\"{x}: {self.children[x]}\" for x in self.children]) + \"}\"
        
    def add(self, word: str) -> None:
        if word == \"\":
            self.exist = True
            return 
        if word[0] not in self.children:
            self.children[word[0]] = TrieNode(word[1:])
        else:
            self.children[word[0]].add(word[1:])
        return
    
    def get_child(self, word: str):
        if word == \"\":
            return self
        if word[0] in self.children:
            return self.children[word[0]].get_child(word[1:])
        return None
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode(None)
        
        max_word_len = 0
        for word in words:
            self.root.add(word[::-1])
            max_word_len = max(max_word_len, len(word))
        
        self.stream = deque(maxlen=max_word_len)
        
    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        
        prefix = list(self.stream)[::-1]
        curr_node = self.root
        for char in prefix:
            if char in curr_node.children:
                if curr_node.children[char].exist == True:
                    return True
                curr_node = curr_node.children[char]
            else:
                return False
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
