class Trie:
    def __init__(self):
        self.dict = {};
        self.isEnd = False;
        
    
class StreamChecker:
    
    def __init__(self, words: List[str]):
        self.root = Trie()
        for i in words:self.insert(i[::-1]);
        self.cur = \"\";
    
    def insert(self,word):
        temp = self.root;
        for i in word:
            if(i not in temp.dict):temp.dict[i] = Trie();
            temp = temp.dict[i];
        temp.isEnd = True;
        return;
    
    def check(self,word):
        temp = self.root;
        word = word[::-1];
        for i in word:
            if(i not in temp.dict):return False;
            temp = temp.dict[i];
            if(temp.isEnd):return True;
        return temp.isEnd;
        
    def query(self, letter: str) -> bool:
        self.cur += letter;
        return self.check(self.cur);
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
