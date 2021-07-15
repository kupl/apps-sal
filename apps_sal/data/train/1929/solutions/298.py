class TrieNode:
    def __init__(self):
        self.children, self.end_node = {}, 0
         
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        root.end_node = 1

class StreamChecker:
    def __init__(self, words):
        self.trie = Trie()
        self.Stream = deque()
        for word in words: self.trie.insert(word[::-1])
         
    def query(self, letter):
        self.Stream.appendleft(letter)
        cur = self.trie.root
        for c in self.Stream:
            if c in cur.children:
                cur = cur.children[c]
                if cur.end_node: return True
            else: break
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
# put all our words to Trie in reversed order
# Imagine we have a current stream abcdefghij and we have dictionary [hij, xyz, abc, hijk] Then what we need to check if some suffix of this word in our dictinonary. It means that jihgfedcba should have jih as prefix. If we add one letter to strim, so we have abcdefghijk, we need to find prefixes in kjihgfedcba and so on.

# Code:

# 1)Trie class with initialization and insert function. Each node has children and flag .end_node, which says if some word ends with this node.
# 2)Put all reversed words to our Trie
# 3)For each new element of stream, we keep it in deque, so we can easily add it to the left of our reversed stream. Then we traverse our Trie and look if we reached some end node.

# Complexity: Let m be the longest length of word and n be number of words. Also let w be number of query(letter). Then space complexity is O(mn + w) to keep our tree. In fact we can cut our deque if it has length more than m, because we never reach nodes which are far in our deque. Time complexity is O(wm), because for each of w queries we need to traverse at most m letters in our trie.

# Note that other method complexity I mentioned in the beginning in theory is also O(wm), but in practise it works like 10 times slower. The problem is with tests like aaaaaa...aaab.
# see DBabichev's explanation. https://leetcode.com/problems/stream-of-characters/discuss/807541/Python-Trie-with-reversed-words-explained

