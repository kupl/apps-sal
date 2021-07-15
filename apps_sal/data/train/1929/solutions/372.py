#class StreamChecker:

    #def _sum_ord(self, word: str):
     #   return sum([ord(c) for c in word])
    
    #def __init__(self, words: List[str]):
        
     #   self.ord_list = [ self._sum_ord(word) for word in words ]
      #  self.curr_ord = 0
       # self.
        #print(self.ord_list)
        
    #def query(self, letter: str) -> bool:
     #   self.curr_ord += ord(letter)
        
      #  if self.curr_ord in self.ord_list:
       #     self.curr_ord = 0
        #    return True
       # else:
        #    return False


class StreamChecker(object):

    def __init__(self, words):
        self.word_map, self.len_map, self.buffer = defaultdict(set), defaultdict(set), \"\"
        for w in words:
            self.word_map[w[-1]].add(w[::-1])
            self.len_map[w[-1]].add(len(w))
        

    def query(self, letter):
        self.buffer = letter + self.buffer
        return any(len(self.buffer) >= l and self.buffer[:l] in self.word_map[letter] for l in self.len_map[letter])
        
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
