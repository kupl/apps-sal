class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            curr = self.trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr['#'] = 1
        self.tmp = [self.trie]

    def query(self, letter: str) -> bool:
        new_tmp = [self.trie]
        flag = False
        for curr in self.tmp:
            if letter in curr:
                curr = curr[letter]
                new_tmp.append(curr)
                if '#' in curr:
                    flag = True
                    if letter in self.trie:
                        new_tmp.append(self.trie[letter])
        self.tmp = new_tmp
        return flag
