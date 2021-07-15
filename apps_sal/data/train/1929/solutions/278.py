class TrieHolder:
    def __init__(self):
        self.flag=0
        self.next=[None]*26

class StreamChecker:
    
    def __init__(self, words: List[str]):
        self.root = TrieHolder()
        for i in words:
            self.insert(i[::-1])
        self.searchLetters=[]
        self.l=0
    
    def insert(self, word: str) -> None:
        t=self.root
        for i in word:
            if t.next[ord(i)-97] == None:
                t.next[ord(i)-97]=TrieHolder()
            t=t.next[ord(i)-97]
        t.flag=1
        
    def query(self, letter: str) -> bool:
        self.searchLetters.append(letter)
        self.l+=1
        t=self.root
        for j in range(self.l-1,-1,-1):
            letter=self.searchLetters[j]
            if t.next[ord(letter)-97]==None:
                return False
            elif t.next[ord(letter)-97].flag==1:
                return True
            else:
                t=t.next[ord(letter)-97]
        return False
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

