class StreamTrie:

    def __init__(self, mychar='ROOT'):
        self.char = mychar
        self.children = {}
        self.mass = 0
        # START WITH EMPTY STRING?
        # self.add('') ??
        if mychar=='ROOT':
            self.max_len = 0
        #self.
    
    #def checkChar(self, nxtChr):
            
    def add(self, word, top_level=True):
        if len(word) == 0:
            self.children['END'] = True
        else:
            self.mass += 1
            c = word[0]
            if not c in self.children:
                self.children[c] = StreamTrie(c)
            self.children[c].add(word[1:],top_level=False)

        if top_level:
            self.max_len = max(self.max_len,len(word))

    def get_max_len(self):
        return self.max_len

    def matches(self,word):
        if len(word) == 0 and 'END' in self.children:
            return True
        if len(word) > 0 and word[0] in self.children:
            return self.children[word[0]].matches(word[1:])
        return False

    def all_matches_from_beginning(self, query_string):
        match_list = []
        first = query_string[0]
        if first in self.children:
            self.children[first]._match_all(query_string,0,match_list)
        return match_list

    def _match_all(self,query_string,cur_ind,match_set):
        #if len(match_set) > 0
        if 'END' in self.children:
            match_set.append(query_string[:(cur_ind+1)])
        #if query_string[ind] == self.char:
        if cur_ind+1 < len(query_string):
            nxt = query_string[cur_ind+1]
            if nxt in self.children:
                self.children[nxt]._match_all(query_string,cur_ind+1,match_set)
        # return

    def any_match_from_beginning(self, query_string):
        #print(query_string)
        return self.children[query_string[0]]._match_any(query_string,0) if query_string[0] in self.children else False
    
    def _match_any(self,query_string,cur_ind):
        #if len(match_set) > 0
        if 'END' in self.children:
            return True
        if cur_ind+1 < len(query_string) and query_string[cur_ind+1] in self.children:
            return self.children[query_string[cur_ind+1]]._match_any(query_string,cur_ind+1)
        else:
            return False

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if 'END' in self.children:
            return f'[{self.char}*]'

        s = f'[{self.char}:{self.mass} '
        if self.char == 'ROOT':
            s = f'Trie({self.mass} '

        kids = []
        for k in self.children:
            if not k == 'END':
                kids.append(str(self.children[k]))
        s += ', '.join(kids)

        s += ')' if self.char == 'ROOT' else ']'

        return s


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = StreamTrie()
        self.longest = 0
        for word in words:
            self.trie.add(word[::-1])
            if len(word) > self.longest:
                self.longest = len(word)
        self.stream = deque()

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        if len(self.stream) > self.longest:
            self.stream.pop()
        #print(self.stream)
        return self.trie.any_match_from_beginning(''.join(self.stream))
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

