class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}
        self.wordMatches = []
class SpellCheckTrie:

    def __init__(self):
        self.root = TrieNode()
        self.exactRoot = TrieNode()
        self.vowelRoot = TrieNode()


    def addWord(self, word):

        it = self.root
        exactIt = self.exactRoot
        vowelIt = self.vowelRoot

        for c in word:
            loweredChar = ord(c) | 32


            vowNormalizedChar = loweredChar
            if c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                vowNormalizedChar = -1 # We use a unique index to reference all vowels
            childNode = it.children.get(loweredChar)
            exactChildNode = exactIt.children.get(ord(c))
            vowelChildNode = vowelIt.children.get(vowNormalizedChar)

            if not childNode:
                childNode = TrieNode()
                it.children[loweredChar] = childNode
            if not exactChildNode:
                exactChildNode = TrieNode()
                exactIt.children[ord(c)] = exactChildNode

            if not vowelChildNode:
                vowelChildNode = TrieNode()
                vowelIt.children[vowNormalizedChar] = vowelChildNode    

            it = childNode
            exactIt = exactChildNode
            vowelIt = vowelChildNode

        it.isWord = True
        it.wordMatches.append(word)
        exactIt.isWord = True
        vowelIt.isWord = True
        vowelIt.wordMatches.append(word)

    def searchWord(self, word):
        it = self.root
        exactIt = self.exactRoot
        vowelIt = self.vowelRoot

        for c in word:
            loweredChar = ord(c) | 32
            vowNormalizedChar = loweredChar
            if c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                vowNormalizedChar = -1
        
            
            if it:
                childNode = it.children.get(loweredChar)
            if exactIt:
                exactChildNode = exactIt.children.get(ord(c))
            if vowelIt:
                vowelChildNode = vowelIt.children.get(vowNormalizedChar)

            if childNode:
                it = childNode
            else:
                it = None
            if exactChildNode:
                exactIt = exactChildNode
            else:
                exactIt = None
                
            if vowelChildNode:
                vowelIt = vowelChildNode
            else:
                vowelIt = None

        if exactIt and exactIt.isWord:
            return word

        if it and it.isWord:
            return it.wordMatches[0]

        if vowelIt and vowelIt.isWord:
            return vowelIt.wordMatches[0]

        return \"\"
    

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        trie = SpellCheckTrie()
        for word in wordlist:
            trie.addWord(word)
            
        return [trie.searchWord(q) for q in queries]
            
        
