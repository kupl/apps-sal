vowels = {'a', 'e', 'i', 'o', 'u'}


class TrieNode:
    def __init__(self):
        self.ch = dict()
        self.words = []
        self.lower_words = defaultdict(list)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for l in word:
            lt = l.lower()
            if lt in vowels:
                lt = 'vowel'
            if lt not in cur.ch:
                cur.ch[lt] = TrieNode()
            cur = cur.ch[lt]
        cur.words.append(word)
        cur.lower_words[word.lower()].append(word)

    def search(self, word):
        cur = self.root
        for l in word:
            lt = l.lower()
            if lt in vowels:
                lt = 'vowel'
            if lt not in cur.ch:
                return ''
            cur = cur.ch[lt]
        if not cur.words:
            return ''
        lw = word.lower()
        if lw in cur.lower_words:
            if word in cur.lower_words[lw]:
                return word
            return cur.lower_words[lw][0]
        return cur.words[0]


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        trie = Trie()
        for word in wordlist:
            trie.insert(word)
        return [trie.search(word) for word in queries]
