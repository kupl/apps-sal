import math
import sys
from itertools import permutations
input = sys.stdin.readline


class Node:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        self.win = False
        self.lose = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, key):
        cur = self.root
        for i in range(len(key)):
            if cur.children[ord(key[i]) - ord('a')] == None:
                cur.children[ord(key[i]) - ord('a')] = Node()
            cur = cur.children[ord(key[i]) - ord('a')]

        cur.isEnd = True

    def search(self, key):
        cur = self.root
        for i in range(len(key)):
            if cur.children[ord(key[i]) - ord('a')] == None:
                return False
            cur = cur.children[ord(key[i]) - ord('a')]

        if cur != None and cur.isEnd:
            return True

        return False

    def assignWin(self, cur):

        flag = True
        for i in range(26):
            if cur.children[i] != None:
                flag = False
                self.assignWin(cur.children[i])

        if flag:
            cur.win = False
            cur.lose = True
        else:
            for i in range(26):
                if cur.children[i] != None:
                    cur.win = cur.win or (not cur.children[i].win)
                    cur.lose = cur.lose or (not cur.children[i].lose)


def __starting_point():

    t = Trie()

    n, k = list(map(int, input().split()))
    for i in range(n):
        s = input()
        if s[-1] == "\n":
            s = s[:-1]
        t.insert(s)

    t.assignWin(t.root)

    if not t.root.win:
        print("Second")
    else:
        if t.root.lose:
            print("First")
        else:
            if k % 2 == 1:
                print("First")
            else:
                print("Second")


__starting_point()
