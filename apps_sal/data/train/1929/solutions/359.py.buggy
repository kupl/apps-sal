class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.letters = []
        # build trie
        for word in words:
            p = self.trie # makre sure point to root for each word
            for ch in word[::-1]:
                if ch not in p:
                    p[ch] = {}
                p = p[ch]
            p['#'] = {}

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        # lookup trie in reverse order
        p = self.trie
        for i in range(len(self.letters) - 1, -1, -1):
            ch = self.letters[i] 
            if ch not in p:
                return False
            p = p[ch]
            if '#' in p:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

\"\"\"
[\"cd\",\"f\",\"kl\"]
        root
     d   f.   l
   c             k

      reverse check <-
a b c d e f g h i j k l
      ^

\"\"\"

