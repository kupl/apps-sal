from collections import defaultdict


class trie:

    def __init__(self):
        (self.nodes1, self.nodes2) = (None, None)
        (self.count1, self.count2) = (0, 0)

    def add(self, s, i):
        if i >= len(s):
            return
        md = int(s[i]) % 2
        if md == 0:
            if not self.nodes1:
                self.nodes1 = trie()
            self.count1 += 1
            self.nodes1.add(s, i + 1)
        else:
            if not self.nodes2:
                self.nodes2 = trie()
            self.count2 += 1
            self.nodes2.add(s, i + 1)

    def remove(self, s, i):
        if i >= len(s):
            return
        md = int(s[i]) % 2
        if md == 0:
            self.count1 -= 1
            self.nodes1.remove(s, i + 1)
            if self.count1 == 0:
                self.nodes1 = None
        else:
            self.count2 -= 1
            self.nodes2.remove(s, i + 1)
            if self.count2 == 0:
                self.nodes2 = None

    def search(self, s, i, mn):
        if i >= len(s):
            return mn
        md = int(s[i]) % 2
        if md == 0:
            if self.nodes1:
                return self.nodes1.search(s, i + 1, min(mn, self.count1))
            else:
                return 0
        elif self.nodes2:
            return self.nodes2.search(s, i + 1, min(mn, self.count2))
        else:
            return 0


t = int(input())
st = set('02468')
mp = defaultdict(int)
res = []
while t > 0:
    t -= 1
    (c, s) = input().split()
    if c == '+':
        ss = ''
        for i in s:
            if i in st:
                ss += '0'
            else:
                ss += '1'
        mp[int(ss, 2)] += 1
    elif c == '-':
        ss = ''
        for i in s:
            if i in st:
                ss += '0'
            else:
                ss += '1'
        mp[int(ss, 2)] -= 1
    elif c == '?':
        res.append(mp[int(s, 2)])
print(*res, sep='\n')
