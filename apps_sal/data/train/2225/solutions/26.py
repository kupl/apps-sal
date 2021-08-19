def main():
    import sys
    input = sys.stdin.readline

    class TreiNode:

        def __init__(self, char_num, depth):
            self.end = False
            self.child = [None] * char_num
            self.depth = depth

        def __setitem__(self, i, x):
            self.child[i] = x

        def __getitem__(self, i):
            return self.child[i]

    class Trei:

        def __init__(self, char_num):
            self.root = TreiNode(char_num, 0)
            self.char_num = char_num

        def add(self, S):
            v = self.root
            for s in S:
                if v[s] is None:
                    v[s] = TreiNode(self.char_num, v.depth + 1)
                v = v[s]
            v.end = True

        def exist(self, S):
            v = self.root
            for s in S:
                if v[s] is None:
                    return False
                v = v[s]
            if v.end:
                return True
            else:
                return False
    (N, L) = list(map(int, input().split()))
    T = Trei(2)
    for _ in range(N):
        S = input().rstrip('\n')
        S = [int(s) for s in S]
        T.add(S)
    g = 0
    st = [T.root]
    while st:
        v = st.pop()
        for i in range(2):
            if v[i] is None:
                d = L - v.depth
                g ^= d & -d
            else:
                st.append(v[i])
    if g:
        print('Alice')
    else:
        print('Bob')


def __starting_point():
    main()


__starting_point()
