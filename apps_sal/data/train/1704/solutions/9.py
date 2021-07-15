class PokerHand(object):

    def __init__(self, hand):
        self.st = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        self.h = sorted(hand.split(), key=lambda x: self.st.index(x[0]))
        self.v=lambda i,j :"Win" if self.st.index(i) > self.st.index(j) else 'Loss'
    
    def compare_with(self, o):
        o = sorted(o.h, key=lambda x: self.st.index(x[0]))
        if o == self.h : return 'Tie'
        s,s1 = [i[0] for i in o],[i[0] for i in self.h]
        a = [self.straight_flush, self.four_of_kind, self.full_house, self.flush, self.straight, self.three_of_kind,self.two_pair, self.one_pair]
        b = [0, 1, 2, self.flush_, self.straight_,5,6, 7]
        for u, j in enumerate(zip(a, b)):
            k,l = j[0],j[1]
            i,j = k(self.h),k(o)
            if i != j : return 'Win' if i else 'Loss'
            elif i == j == 1 : 
                if u in [3,4] : return l(s1,s) 
                return self.common(s1, s)
        for i, j in zip(s1[::-1], s[::-1]):
            if i != j : return self.v(i,j)
        return 'Tie'
    
    def straight_flush(self, p):
        return len(set([i[1] for i in p])) == 1 and all(abs(self.st.index(p[i][0]) - self.st.index(p[i + 1][0])) == 1 for i in range(len(p) - 1))

    def four_of_kind(self, p):
        p = [i[0] for i in p]
        return any(p.count(i) == 4 for i in p)

    def full_house(self, p):
        p = [i[0] for i in p]
        return any(p.count(i) == 3 for i in p) and any(p.count(i) == 2 for i in p)

    def flush(self, p):
        return len(set([i[1] for i in p])) == 1

    def straight(self, p):
        return all(abs(self.st.index(p[i][0]) - self.st.index(p[i + 1][0])) == 1 for i in range(len(p) - 1))

    def three_of_kind(self, p):
        p = [i[0] for i in p]
        return any(p.count(i) == 3 for i in p)

    def two_pair(self, p):
        p = [i[0] for i in p]
        return [p.count(i) for i in set(p)].count(2) == 2

    def one_pair(self, p):
        p = [i[0] for i in p]
        return [p.count(i) for i in set(p)].count(2) == 1

    def high_card(self, p):
        p = [i[0] for i in p]
        return max(p, key=lambda x: self.st.index(x))

    def straight_flush_(self, i, j):
        return 'Win' if self.v(i[-1],j[-1]) else 'Loss'

    def common(self,i,j):
        findi = sorted([k for k in set(i)], key=lambda x: (-i.count(x), -self.st.index(x)))
        findj = sorted([k for k in set(j)], key=lambda x: (-j.count(x), -self.st.index(x)))
        for k, l in zip(findi, findj):
            if k != l : return 'Win' if self.st.index(k) > self.st.index(l) else 'Loss'
                
    def flush_(self, i, j):
        for k, l in zip(i[::-1], j[::-1]):
            if k != l : return 'Win' if self.st.index(k) > self.st.index(l) else 'Loss'

    def straight_(self, i, j):
        return 'Tie' if self.st.index(i[-1]) == self.st.index(j[-1]) else 'Win' if self.st.index(i[-1]) > self.st.index(j[-1]) else 'Loss'
