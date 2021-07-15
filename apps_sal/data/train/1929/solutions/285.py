class TrieNode:
    
    def __init__(self, val  =   \"\"):
        self.val    =   val;
        self.next_chars =   collections.defaultdict(str);
        self.end_of_word    =   False;
        return;

class Trie:
    
    def __init__(self, words):
        self.head       =   TrieNode(\"head\");
        self.curr_ptr   =   self.head;
        
        for w in words:
            self._add_word(w);
            
        return;
    
    def check_char(self, c):
        ptr =   self.curr_ptr;
        
        if c not in ptr.next_chars:
            self.curr_ptr   =   self.head;
            if c in self.curr_ptr.next_chars:
                self.curr_ptr   =   self.head.next_chars[c];
            return False;
        
        self.curr_ptr   =   ptr.next_chars[c];
        return True;
    
    def ptr_end_of_word(self):
        return self.curr_ptr.end_of_word;
    
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
    def __init__(self, words: List[str]):
        
        self.trie_words =   Trie(words);      
        

    def query(self, letter: str) -> bool:
        
        ptr =   self.trie_words.curr_ptr;
  
        #print(letter, ptr.val, ptr.end_of_word);

        
        check_letter        =   self.trie_words.check_char(  letter);
        check_end_of_word   =   self.trie_words.ptr_end_of_word();
        
        #print(  letter, check_letter,   check_end_of_word);
        return  check_letter    and  check_end_of_word;

    \"\"\"
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
