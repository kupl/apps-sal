class TrieNode:
    def __init__(self,letter):
        self.letter=letter
        self.next_alpha={}
        self.end=False

class StreamChecker:

    def __init__(self, words: List[str]):

        self.root=TrieNode('root')
        self.stream=deque()

        self.p=None
        
        for word in words:
            buffer=TrieNode('a')
            if(len(word)==1):
                self.root.next_alpha[word[0]]=TrieNode(word[0])
                self.root.next_alpha[word[0]].end=True
                continue
                
            for letter_ind,l in enumerate(word[::-1]):
                if(letter_ind==0):
                    if(l not in list(self.root.next_alpha.keys())):
                        self.root.next_alpha[l]=TrieNode(l)
                        
                    buffer=self.root.next_alpha[l]
                    continue
                
                if(l in list(buffer.next_alpha.keys())):
                    buffer=buffer.next_alpha[l]
                else:
                    
                    nex=TrieNode(l)
                    buffer.next_alpha[l]=nex
                    buffer=nex
                
                
                if(letter_ind==len(word)-1):
                    buffer.end=True
        
        
    def query(self, letter: str) -> bool:

        self.stream.appendleft(letter)
        cur=self.root
        
        for c in self.stream:
            if c in cur.next_alpha:
                cur = cur.next_alpha[c]
                if cur.end: return True
            else: break
        return False
            
            
        '''
        print(letter,end=\"->\")
        if(self.p==None):
            if(letter not in self.root.next_alpha.keys()):
                return False
            
            self.p=self.root.next_alpha[letter]
            
            
                
        else:
            if(letter in self.p.next_alpha.keys()):
                self.p=self.p.next_alpha[letter]
                print(\"next\")
            else:
                if(letter not in self.root.next_alpha.keys()):
                    return False
                self.p=self.root.next_alpha[letter]
                print(\"reset\")

            

        print(self.p.end)
        return self.p.end

        '''
        
        

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

