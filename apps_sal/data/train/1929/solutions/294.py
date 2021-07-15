class TrieNode:
    def __init__(self, val):
        self.val = val
        self.branches = dict()
    def query(self, word):
        \"\"\"
        returns true if and only if for some k >= 1, the last k characters of the string WORD is in the trie 
        \"\"\"
        # print(\"querying\", word)
        if \"*\" in self.branches:
            # print(\"found word\")
            return True
        if word and word[-1] in self.branches:
            return self.branches[word[-1]].query(word[:-1])
        return False
        
    def addWord(self, word):
        if not word:
            self.branches[\"*\"] = TrieNode('*')
        else:
            next_letter = word[-1]
            if next_letter not in self.branches:
                self.branches[next_letter] = TrieNode(next_letter)
            self.branches[next_letter].addWord(word[:-1])
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = TrieNode(\"head\")
        for w in words:
            self.trie.addWord(w)
        self.stream = \"\"

    def query(self, letter: str) -> bool:
        self.stream += letter
        return self.trie.query(self.stream)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
