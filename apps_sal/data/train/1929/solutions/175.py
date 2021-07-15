class TrieNode:
    def __init__(self):
        self.children={}
        self.terminal=False

class Trie(object):

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.root = TrieNode()

    def insert(self, word):
        \"\"\"
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        \"\"\"
        if len(word) <= 0:
            return
        
        trav = self.root
        for i in range(len(word)):
            if word[i] in trav.children:
                trav = trav.children[word[i]]
            else:
                trav.children[word[i]] = TrieNode()
                trav = trav.children[word[i]]
        trav.terminal = True

class StreamChecker:
    # reference: https://leetcode.com/problems/stream-of-characters/discuss/320837/Easily-implemented-Python-Trie-Solution
    def __init__(self, words: List[str]):
        self.queries = []
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        # basically returns false if the letter is the oldest letter of the world
        # keep tracks of all queries from oldest to newest
        self.queries.append(letter)
        i = len(self.queries) - 1
        node = self.trie.root
        
        # iterate from the end so we are looking at the newest queries first
        # since word is saved backwords, it will return True
        while i >= 0:
            # already an end of a word
            if node.terminal:
                return True
            # there is no prefix of this
            if self.queries[i] not in node.children:
                return False
            node = node.children[self.queries[i]]
            i -= 1
        return node.terminal
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
