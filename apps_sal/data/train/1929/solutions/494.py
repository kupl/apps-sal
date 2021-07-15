class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie={}
        node=self.trie
        for i in words:
            for ch in i[::-1]:
                if ch not in node:
                    node[ch]={}
                node=node[ch]
            node['$']=True
            node=self.trie
        self.stream=''
        

    def query(self, letter: str) -> bool:
        self.stream+=letter
        node=self.trie
        def check(s,node):
            if '$' in node:
                return True
            for ch in s:
                if ch in node:
                    return check(s[1:],node[ch])
                else:
                    return False
        return check(self.stream[::-1],node)
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

