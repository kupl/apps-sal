class StreamChecker:

    def __init__(self, words: List[str]):
        self.word_tree = dict()
        self.stream = []
        self.min_len = float(\"inf\")
        
        rev_words = sorted([word[::-1] for word in words])
        
        for word in rev_words:
            self.min_len = min(self.min_len, len(word))
            cur_dict = self.word_tree
            for c in word[:-1]:
                if c not in cur_dict:
                    cur_dict[c] = (False, dict())
                    
                cur_dict = cur_dict[c][1]
                
            if word[-1] not in cur_dict:
                cur_dict[word[-1]] = (True, dict())
            else:
                last_entry = cur_dict[word[-1]]
                cur_dict[word[-1]] = (True, last_entry[1])
                

    def query(self, letter: str) -> bool:
        self.stream.insert(0, letter)
        
        if len(self.stream) < self.min_len: return False
        
        cur_dict = self.word_tree
        for c in self.stream:
            if c in cur_dict and cur_dict[c][0]:
                return True
            elif c in cur_dict:
                cur_dict = cur_dict[c][1]
            else:
                return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
