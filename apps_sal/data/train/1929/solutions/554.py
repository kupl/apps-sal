from collections import defaultdict
class StreamChecker:

    def __init__(self, words: List[str]):
        
        self.words=words
        self.rev_words={}
        self.n=0
        self.cur_word=''
        self.dic=defaultdict(list)
        
        for i,word in enumerate(words):
            rev_word=word[::-1]
            self.rev_words[i]=rev_word
            self.dic[rev_word[0]].append(i)
            
            if len(word)>self.n:
                self.n=len(word)        
        
        #print(self.rev_words)
        #print(self.dic)
    
    def query(self, letter: str) -> bool:
        
        if len(self.cur_word)==self.n:
            self.cur_word=self.cur_word[1:]
        
        self.cur_word+=letter
        
        #print(self.cur_word)
        
        if letter in self.dic:
            index=self.dic[letter]
            
            for i in index:
                word=self.rev_words[i]
                
                if len(word)<=len(self.cur_word):
                    if self.cur_word[::-1][:len(word)]==word:
                        #print(self.cur_word,word)
                        return True
            
        return False
                        

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

