class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.val = -1

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        current = self.root
        for char in word:
            current = current.children[char]

        current.val = 10
    def search(self, word):
        current = self.root
        for char in word:
            current = current.children.get(char)
            if not current:
                return False
        return current.val > 1
    def starts_with(self, word):
        current = self.root
        for char in word:
            current = current.children.get(char)
            if not current:
                return False
        return True
    

class StreamChecker:

    # O(NW) where N is number of words
    # Q is maxlength of word
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.letters = []
        for word in words:
            # insert in reverse order to check for Trie keys as soon as new node is added
            self.trie.insert(word[::-1])

    #waiting.size <= W, where W is the maximum length of words.
    # So that O(query) = O(waiting.size) = O(W)
    # for q queries, O(QW)
    def query(self, letter: str) -> bool:
        self.letters += letter
        i = len(self.letters) - 1
        node = self.trie.root
        curr_word = ''
        for i in range(len(self.letters) - 1, -1, -1):
            curr_word += self.letters[i]
            has_sub_word = self.trie.starts_with(curr_word)
            if not has_sub_word:
                return False
            if has_sub_word and self.trie.search(curr_word):
                return True
        return False
#         while i >= 0:
#             # if any of the word matches return True
#             if node.val > 1:
#                 return True
#             if self.letters[i] not in node.children:
#                 return False
#             node = node.children[self.letters[i]]
#             i -= 1
        
#         return node.val > 1
    


