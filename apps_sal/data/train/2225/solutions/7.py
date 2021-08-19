# nimber: 0, 1, 2, 1, 4, 1, 2, 1, 8, 1, 2, 1, 4, 1, 2, 1, 16, 1, 2, 1, 4, 1, 2, 1, 8, 1, 2, 1, 4, 1, 2, 1, 32, ...

class Node:
    def __init__(self, size, avail):
        self.end = False
        self.nxt = [None] * size
        self.avail = avail

    def __setitem__(self, i, x): self.nxt[i] = x
    def __getitem__(self, i): return self.nxt[i]


def makeTrie(strs, size):
    root = Node(size, l)
    for s in strs:
        n = root
        for c in s:
            i = int(c)  # Change this to adapt. ex: ord(c)-ord("A")
            if not n[i]:
                n[i] = Node(size, n.avail - 1)
            n = n[i]
        n.end = True
    return root


def nimber(n):
    x = 1
    while n % 2 == 0:
        n //= 2
        x *= 2
    return x


input = __import__('sys').stdin.readline
n, l = map(int, input().split())
strs = [input().rstrip() for i in range(n)]
T = makeTrie(strs, 2)

ans = 0
stack = [T]
while stack:
    n = stack.pop()
    for i in 0, 1:
        if not n[i]:
            ans ^= nimber(n.avail)
        elif not n[i].end:
            stack.append(n[i])
print("Alice" if ans else "Bob")
