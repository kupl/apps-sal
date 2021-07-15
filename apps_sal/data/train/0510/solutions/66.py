class Segment_tree():
    def __init__(self, n, s):
        self.alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.key = dict()
        self.k = 1
        for value in self.alphabet_list:
            self.key[value] = self.k
            self.k *= 2
        self.inf = pow(2, 32)
        self.n = n
        self.s = s
        self.N = 1
        while self.N < self.n:
            self.N *= 2
        self.size = self.N * 2
        self.size -= 1
        self.N -= 1
        self.segment = [0]*(self.N) + [self.key[self.s[i]] for i in range(self.n)] + [0]*(self.size-self.N-self.n)
        for i in range(self.N-1, -1, -1):
            self.segment[i] = self.segment[2*i+1]|self.segment[2*i+2]

    def update(self, i, x):
        i += (self.N-1)
        self.segment[i] = self.key[x]
        while i > 0:
            i = (i-1)//2
            self.segment[i] = self.segment[2*i+1]|self.segment[2*i+2]
        
    def find(self, a, b, k, l, r):
        if r <= a or b <= l:
            return 0
        elif a <= l and r <= b:
            return self.segment[k]
        else:
            find_l = self.find(a, b, 2*k+1, l, (l+r)//2)
            find_r = self.find(a, b, 2*k+2, (l+r)//2, r)
            return find_l|find_r


n = int(input())
s = input()
segment = Segment_tree(n, s)
q = int(input())
N = 1
while N < n:
  N *= 2
for i in range(q):
    quer = [x for x in input().split()]
    if quer[0] == "1":
        i, c = int(quer[1]), quer[2]
        segment.update(i, c)
    else:
        l, r = int(quer[1]), int(quer[2])
        key = segment.find(l-1, r, 0, 0, N)
        ans = 0
        for i in range(26):
            if (key>>i)&1:
                ans += 1
        print(ans)
