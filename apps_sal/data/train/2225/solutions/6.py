from collections import deque
# 節の定義


class Node:
    def __init__(self, x):
        self.data = int(x)
        self.left = None
        self.right = None
# 挿入


def insert(node, x):
    ima = node
    for i in range(len(x)):
        y = x[i]
        if y == "1":
            if ima.right is None:
                ima.right = Node(i + 1)
            ima = ima.right
        else:
            if ima.left is None:
                ima.left = Node(i + 1)
            ima = ima.left


class Trie:
    def __init__(self):
        self.root = Node(0)

    # 挿入
    def insert(self, x):
        insert(self.root, x)


n, l = map(int, input().split())
s = [input() for i in range(n)]

trie = Trie()
for i in s:
    trie.insert(i)
data = []
que = deque([trie.root])


def dfs(node):
    if node.right is None and node.left is None:
        return 0
    if node.right is None or node.left is None:
        if l - node.data:
            data.append(l - node.data)
    if node.right:
        que.append(node.right)
    if node.left:
        que.append(node.left)


while que:
    dfs(que.popleft())
xor = 0


def nimber(n):
    x = 1
    while n % 2 == 0:
        n //= 2
        x *= 2
    return x


for i in data:
    xor ^= nimber(i)
print("Alice" if xor else "Bob")
