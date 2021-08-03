class dsu:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [0 for x in range(n)]
        self.valid = [True for x in range(n)]
        self.n = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, s, t):
        sp, tp = self.find(s), self.find(t)
        if sp == tp:
            return
        if self.rank[sp] < self.rank[tp]:
            self.parent[sp] = tp
        elif self.rank[sp] > self.rank[tp]:
            self.parent[tp] = sp
        else:
            self.parent[tp] = sp
            self.rank[sp] += 1

    def cluster(self):
        for x in range(self.n):
            self.find(x)


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        arrlen = len(transactions)
        net = dsu(arrlen)
        tplist = [t.split(',') for t in transactions]
        for i in range(arrlen):
            tp = tplist[i]
            name, time, amt, city = tp[0], tp[1], tp[2], tp[3]
            if int(amt) > 1000:
                net.valid[i] = False
            for j in range(i + 1, arrlen):
                jtp = tplist[j]
                jname, jtime, jamt, jcity = jtp[0], jtp[1], jtp[2], jtp[3]
                if jname == name and jcity != city and abs(int(jtime) - int(time)) <= 60:
                    net.union(i, j)
        net.cluster()
        for i in range(arrlen):
            if net.parent[i] != i or net.rank[i] != 0:
                net.valid[i] = False
        return [transactions[i] for i in range(arrlen) if not net.valid[i]]
