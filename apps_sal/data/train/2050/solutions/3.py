import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


class Trie:

    def __init__(self):
        self.arr = {}

    def insert(self, word):
        root = self
        for x in word:
            if x not in root.arr:
                root.arr[x] = Trie()
            root = root.arr[x]

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
if k == 1:
    answer(win)
elif not win:
    answer(win)
elif lose:
    answer(win)
elif k & 1:
    answer(win)
else:
    answer(not win)
