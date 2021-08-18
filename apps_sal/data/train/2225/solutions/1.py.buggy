import sys
#from collections import defaultdict
sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()[:-1]


n, l = list(map(int, input().split()))
ss = [list(input())[::-1] for _ in range(n)]


def addTree(tree, sentence):
    if not sentence:
        return None

    if sentence[-1] not in tree:
        tree[sentence[-1]] = {}

    p = sentence.pop()
    tree[p] = addTree(tree[p], sentence)

    return tree


def createTree(sentences):
    tree = {}
    for sentence in sentences:
        tree = addTree(tree, sentence)

    return tree


tree = createTree(ss)
# print(tree)

grundy = 0


def dfs(cur, level):
    nonlocal grundy
    if cur is None:
        return
    elif len(cur) == 1:
        grundy ^= (l - level) & (-l + level)
    for k in list(cur.keys()):
        dfs(cur[k], level + 1)
    return


dfs(tree, 0)

if grundy == 0:
    print("Bob")
else:
    print("Alice")
