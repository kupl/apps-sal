import sys
input = sys.stdin.readline
s = input()
M = int(input())


def next_pow_2(n):
    p = 1
    while p < n:
        p <<= 1
    return p


def represented_range(node, size):
    l = node
    r = node
    while l < size:
        l = 2 * l
        r = 2 * r + 1
    return (l - size, r - size)


class SegTree:

    def __init__(self, size):
        self.size = next_pow_2(size)
        self.answer = [0] * (2 * self.size)
        self.opened = [0] * (2 * self.size)
        self.closed = [0] * (2 * self.size)

    def build(self, s):
        for i in range(self.size):
            self.answer[self.size + i] = 0
            self.opened[self.size + i] = 1 if i < len(s) and s[i] == '(' else 0
            self.closed[self.size + i] = 1 if i < len(s) and s[i] == ')' else 0
        for i in range(self.size - 1, 0, -1):
            matched = min(self.opened[2 * i], self.closed[2 * i + 1])
            self.answer[i] = self.answer[2 * i] + self.answer[2 * i + 1] + matched
            self.opened[i] = self.opened[2 * i] + self.opened[2 * i + 1] - matched
            self.closed[i] = self.closed[2 * i] + self.closed[2 * i + 1] - matched

    def query(self, l, r):
        l += self.size
        r += self.size
        eventsL = []
        eventsR = []
        while l <= r:
            if l & 1:
                eventsL.append((self.answer[l], self.opened[l], self.closed[l]))
                l += 1
            if not r & 1:
                eventsR.append((self.answer[r], self.opened[r], self.closed[r]))
                r -= 1
            l >>= 1
            r >>= 1
        answer = 0
        opened = 0
        for (a, o, c) in eventsL + eventsR[::-1]:
            matched = min(c, opened)
            answer += a + matched
            opened += o - matched
        return answer


seg = SegTree(len(s))
seg.build(s)
for i in range(M):
    (l, r) = [int(_) for _ in input().split()]
    print(2 * seg.query(l - 1, r - 1))
