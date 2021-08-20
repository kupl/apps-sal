import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


class Trie:

    def __init__(self):
        self.arr = {}

    def insert(self, word):
        for x in word:
            if x not in self.arr:
                self.arr[x] = Trie()
            self = self.arr[x]

    def dfs(self):
        if not len(self.arr):
            return (False, True)
        (win, lose) = (False, False)
        for x in self.arr:
            (w, l) = self.arr[x].dfs()
            win = win or not w
            lose = lose or not l
        return (win, lose)


def answer(flag):
    print('First' if flag else 'Second')


T = Trie()
(n, k) = list(map(int, input().split()))
for _ in range(n):
    T.insert(input())
(win, lose) = T.dfs()
if k == 1 or not win or lose or k & 1:
    answer(win)
else:
    answer(not win)
