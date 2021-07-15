
class StreamChecker:
    '''based on trie
       the core idea TLE is to create the trie with words in reverse order. also create a buffer that is used durring the query
    '''
    def __init__(self, words: List[str]):
        self.s = ''
        self.dic = defaultdict(set)
        for w in words:
            self.dic[w[-1]].add(w)

    def query(self, letter: str) -> bool:
        self.s += letter
        return any(self.s.endswith(w) for w in self.dic[letter])
