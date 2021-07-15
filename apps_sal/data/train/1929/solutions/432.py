class TrieNode:
    
    def __init__(self, val  =   \"\"):
        self.val    =   val;
        self.next_chars =   collections.defaultdict(str);
        self.end_of_word    =   False;
        return;

class Trie:
    
    def __init__(self, words):
        self.head       =   TrieNode(\"head\");
        
        for w in words:
            self._add_word(w[::-1]);
            
        return;
    
    def check_word(self, word):
        
        ptr =   self.head;
        for c in word[::-1]:
            
            if c not in ptr.next_chars:     return False;            
            
            ptr =   ptr.next_chars[c];
            
            if ptr.end_of_word:           return True;
            
        
        return ptr.end_of_word;
        
        
    def _add_word(self, word):
        
        ptr =   self.head;
        
        for c in word:
            
            if c not in ptr.next_chars:
                ptr.next_chars[c]   =   TrieNode(c);
            
            ptr =   ptr.next_chars[c];
        
        ptr.end_of_word =   True;
        
        return;

MAX_LENGTH  =   2001;

class StreamChecker:
    
    def __init__(self, words: List[str]):
        
        self.trie_words =   Trie(words);
        self.rolling_word   =   [];
        return;
        

    def query(self, letter: str) -> bool:
        
        self.rolling_word.append(   letter);
        
        result  =   self.trie_words.check_word( self.rolling_word);
            
        
        if len(self.rolling_word) >= MAX_LENGTH:    self.rolling_word.pop(0);
        
        return result;
    
    
    
    \"\"\"
    ############## BRUTE FORCE ##############################
    def __init__    (self, words):
        
        self.last_char_words    =   collections.defaultdict(set);
        self.rolling_word       =   \"\";
        
        for w in words:
            last_c  =   w[-1];
            self.last_char_words.setdefault(last_c, set()).add(w);
        
        #print(self.last_char_words);
        return;
    
    def query(  self, letter:str)   -> bool:
        
        self.rolling_word += letter;
        
        for w in self.last_char_words[letter]:
            ln_w    =   len(w);
            
            if self.rolling_word[-ln_w:] == w:
                return True;
        
        self.rolling_word   =   self.rolling_word[-MAX_LENGTH:];
        return False;
    \"\"\"
    


    


        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
