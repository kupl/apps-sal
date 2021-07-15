class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie={}
        # self.min=40000
        self.searchWord=''
        for word in words:
            word=word[::-1]
            # self.min=len(word) if len(word)<self.min else self.min
            self.insertToTrie(self.trie, word)
            
    def insertToTrie(self, trie, word):
        if word[0] not in trie:
            trie[word[0]] = {\"value\":{}, \"isLast\":len(word)==1}
        if len(word)==1:
            trie[word[0]][\"isLast\"] = True
            return
        self.insertToTrie(trie[word[0]][\"value\"], word[1:])
            
    def searchForWord(self, trie, word):
        if not word or word[0] not in trie:
            return False
        if trie[word[0]][\"isLast\"]:
            return True
        return self.searchForWord(trie[word[0]][\"value\"], word[1:])

    def query(self, letter: str) -> bool:
        # if(self.min):
        #     self.min-=1
        #     return False
        self.searchWord = letter + self.searchWord
        result = self.searchForWord(self.trie, self.searchWord)
        return result


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
