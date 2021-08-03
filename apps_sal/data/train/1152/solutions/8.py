class TrieNode():
    def __init__(self):
        self.children = [None] * 27
        self.ispresent = 0
        self.priority = "aa"
        self.index = -1


class Trie():
    def __init__(self):
        self.root = self.getnode()

    def getnode(self):
        return TrieNode()

    def getind(self, ch):
        if ch == '-':
            return 26
        return ord(ch) - 97

    def insert(self, key, pos, pri):
        curr = self.root
        l = len(key)
        for i in range(l):
            place = self.getind(key[i])
            if curr.children[place] == None:
                curr.children[place] = self.getnode()
                curr = curr.children[place]
                curr.index = pos
                curr.priority = pri
            else:
                curr = curr.children[place]
                if pri > curr.priority:
                    curr.priority = pri
                    curr.index = pos
        curr.ispresent = 1

    def search(self, key):
        curr = self.root
        l = len(key)
        for i in range(l):
            place = self.getind(key[i])
            if curr.children[place] == None:
                return -1
            curr = curr.children[place]
        return curr.index


data = Trie()
n = int(input())
strings = []
for i in range(n):
    string, pri = input().split()
    pri = int(pri)
    data.insert(string, i, pri)
    strings.append(string)
q = int(input())
for i in range(q):
    start = input()
    ans = data.search(start)
    if ans == -1:
        print('NO')
    else:
        # print(ans,start)
        print(strings[ans])
