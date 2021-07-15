class StreamChecker:
# with the trie like #ba and baa 
# before my solution when it fit ba, it will set the curr the self.trie['a'] again, which will miss the potential of baa， need a structure to preserve all possible curr

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            curr = self.trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr['#'] = 1
        #self.curr = self.trie
        self.tmp = [self.trie]


    def query(self, letter: str) -> bool:
        new_tmp = [self.trie]
        flag = False
        for curr in self.tmp:
            if letter in curr:
                curr = curr[letter]
                new_tmp.append(curr)
                #check if it's the end
                if '#' in curr: 
                    flag = True
                    if letter in self.trie:
                        new_tmp.append(self.trie[letter])      

            #else:
                #self.curr = self.trie
            #    new_tmp.append(self.trie)
        self.tmp = new_tmp

        return flag


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)





