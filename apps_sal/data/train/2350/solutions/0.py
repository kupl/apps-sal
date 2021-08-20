"""
#this code is a precomputation part.
#it takes about 2 hours.
class Graph:
  def __init__(self,n):
    self.edge=[[0 for j in xrange(n)] for i in xrange(n)]
    self.n=n

  def addedge(self,i,j,m=1):
    assert i!=j and 0<=i<self.n and 0<=j<self.n
    self.edge[i][j]+=m
    self.edge[j][i]+=m

  def deledge(self,i,j,m=1):
    assert i!=j and 0<=i<self.n and 0<=j<self.n
    self.edge[i][j]-=m
    self.edge[j][i]-=m

  def strongconnect(self):
    ret = True
    n=self.n
    for i in xrange(n):
      for j in xrange(i+1,n):
        if self.edge[i][j]:
          self.deledge(i,j)
          ret=self.connect()
          self.addedge(i,j)
          if ret==False:return ret
    return True

  def connect(self):
    n=self.n
    edge=self.edge
    z=[0 for _ in xrange(n)]
    def f(i):
      assert 0<=i<n
      if z[i]==1:return
      z[i]=1
      for j in xrange(n):
        if edge[i][j]:f(j)
    f(0)
    return sum(z)==n

  def Nconnect(self):
    n=self.n
    edge=self.edge
    z=[0 for _ in xrange(n)]
    def f(i):
      assert 0<=i<n
      if z[i]==1:return
      z[i]=1
      for j in xrange(n):
        if edge[i][j]:f(j)
    ret=0
    for ver in xrange(n):
      if z[ver]==0:
        ret+=1
        f(ver)
    return ret

def search(nv,ne):
  graph=Graph(nv)
  init=( graph, (0,0), ne)
  def f(state):
    ret=0
    g,(i,j),e=state
    if e==0:
      if g.strongconnect():
        return fact(ne)
      else:return 0

    if e<g.Nconnect():
      return 0
    for i2 in xrange(nv):
      for j2 in xrange(i2+1,nv):
        if (i2,j2)>(i,j):
          for k in xrange(1,e+1):
            g.addedge(i2,j2,k)
            ret += f((g,(i2,j2),e-k)) / fact(k)
            g.deledge(i2,j2,k)
    return ret
  return f(init)

def fact(n):
  assert n>=0
  ret=1
  for i in xrange(n):ret*=i+1
  return ret

def comb(a,b):
  return fact(a+b)/fact(a)/fact(b)
  pass

nnn=17
sve=dict( ( (v,e),search(v,e) )  for v in xrange(nnn+1) for e in xrange(nnn+1) if e>=v and e+v<=nnn)
sve[(1,0)]=1
print sve
"""
output = '\n{(6, 9): 10559808000, (0, 7): 0, (1, 6): 0, (0, 10): 0, (3, 7): 2142, (2, 5): 1, (1, 11): 0, (5, 8): 48094200, (6, 7): 6350400, (5, 5): 1440, (6, 10): 247973140800, (0, 17): 0, (0, 4): 0, (1, 1): 0, (4, 10): 57808440, (2, 6): 1, (5, 11): 84587745000, (4, 5): 2160, (0, 1): 0, (3, 12): 531366, (1, 12): 0, (2, 11): 1, (7, 8): 482630400, (0, 14): 0, (3, 11): 177078, (1, 15): 0, (8, 9): 45113241600, (4, 12): 2148847272, (2, 12): 1, (1, 16): 0, (1, 5): 0, (0, 11): 0, (3, 6): 690, (2, 2): 1, (1, 10): 0, (6, 11): 4928158065600, (0, 5): 0, (1, 0): 1, (0, 8): 0, (4, 11): 354158640, (3, 5): 210, (2, 7): 1, (5, 10): 7639380000, (4, 6): 25560, (5, 7): 2835000, (0, 2): 0, (1, 3): 0, (4, 8): 1433544, (2, 8): 1, (0, 15): 0, (3, 10): 58986, (1, 14): 0, (4, 13): 12970756656, (2, 13): 1, (1, 4): 0, (0, 12): 0, (3, 9): 19626, (2, 3): 1, (1, 9): 0, (2, 14): 1, (6, 8): 336268800, (0, 6): 0, (1, 7): 0, (0, 9): 0, (3, 4): 54, (2, 4): 1, (5, 9): 644550480, (4, 7): 206640, (6, 6): 43200, (5, 6): 104400, (7, 7): 1814400, (0, 16): 0, (0, 3): 0, (3, 14): 4782882, (1, 2): 0, (4, 9): 9265200, (3, 3): 6, (2, 9): 1, (5, 12): 900380296200, (4, 4): 72, (7, 10): 2379856852800, (0, 0): 1, (3, 13): 1594242, (1, 13): 0, (2, 10): 1, (7, 9): 44808422400, (0, 13): 0, (3, 8): 6510, (1, 8): 0, (8, 8): 101606400, (2, 15): 1}\n'
sve = eval(''.join(output.split('\n')))


def fact(n):
    assert n >= 0
    ret = 1
    for i in range(n):
        ret *= i + 1
    return ret


def comb(a, b):
    return fact(a + b) / fact(a) / fact(b)
    pass


'python 2.5 cannot use fractions.'
'I used fractions for local computation.'
memo_ff = {}


def powpoly(x, t):
    ret = [1] + [0] * (len(x) - 1)
    n = len(x)
    for _ in range(t):
        ret2 = [0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i + j < n:
                    ret2[i + j] += ret[i] * x[j]
        ret = ret2
    return ret


def ing(x):
    n = len(x)
    assert x[0] == 0
    ret = [0 for _ in range(n)]
    for t in range(0, n):
        ret2 = powpoly(x, t)
        for i in range(n):
            ret[i] += fr * ret2[i] / fact(t)
    return ret


def ff(Y):
    if Y in memo_ff:
        return memo_ff[Y]
    t = Y[0]
    if t == 0:
        n = Y[1]
        ret = 0
        for (v, e) in sve:
            if v + e > n or v == 0:
                continue
            val = sve[v, e]
            for l1 in range(n - v + 1):
                l2 = n - v - l1
                p1 = ff((2, l1, e))
                p2 = ff((3, l2, v))
                a = fr * val * fact(n - 1) / fact(v - 1) / fact(l1) / fact(l2) * p1 * p2 / fact(e)
                ret += a
    elif t == 1:
        n = Y[1]
        ret = 0
        for (v, e) in sve:
            val = sve[v, e]
            e -= 1
            if e == -1 or v + e > n or v == 0:
                continue
            for l1 in range(n - v + 1):
                l2 = n - v - l1
                p1 = ff((2, l1, e))
                p2 = ff((3, l2, v))
                ret += fr * val * fact(n) / fact(v) / fact(l1) / fact(l2) * p1 * p2 / fact(e)
    elif t == 2:
        n = Y[1]
        e = Y[2]
        F = [fr * i * ff((0, i)) / fact(i) for i in range(n + 1)]
        Fa = powpoly(F, e)
        ret = Fa[n] * fact(n)
    elif t == 3:
        n = Y[1]
        v = Y[2]
        G = [v * fr * ff((1, i)) / fact(i) for i in range(n + 1)]
        Ga = ing(G)
        ret = Ga[n] * fact(n)
    memo_ff[Y] = ret
    return ret


memo = {}


def g(Y):
    if Y in memo:
        return memo[Y]
    (k, c) = Y
    if c == 0:
        return ff((0, k))
    if 2 * c >= k:
        return 0
    ret = 0
    for k1 in range(1, 18):
        for k2 in range(1, 18):
            k3 = k - k1 - k2
            if k3 <= 0:
                break
            for c1 in range(18):
                if 2 * c1 >= k1:
                    break
                for c2 in range(18):
                    if 2 * c2 >= k2:
                        break
                    c3 = c - 1 - c1 - c2
                    if 2 * c3 >= k3:
                        continue
                    ret += g((k1, c1)) * g((k2, c2)) * g((k3, c3)) * fact(k1 + k2 + k3) / fact(k1) / fact(k2) / fact(k3) * k1 * k2 * k3
    r = ret / (6 * c)
    memo[Y] = r
    return r


def ans(n):
    return sum((g((n, i)) for i in range(n)))


def brute(n):
    m = [(i1, i2, i3) for i1 in range(n) for i2 in range(i1 + 1, n) for i3 in range(i2 + 1, n)]
    init = []
    memob = {}

    def f(vs):
        ret = 0
        if vs:
            g = Graph(n)
            for v in vs:
                (i1, i2, i3) = v
                g.addedge(i1, i2)
                g.addedge(i1, i3)
            a = g.Nconnect()
            for notv in vs:
                g = Graph(n)
                for v in vs:
                    if v == notv:
                        continue
                    (i1, i2, i3) = v
                    g.addedge(i1, i2)
                    g.addedge(i1, i3)
                if g.Nconnect() == a:
                    return 0
            if a == 1:
                return 1
        ret = 0
        for v in m:
            if len(vs) == 0 or v > vs[-1]:
                ret += f(vs + [v])
        return ret
    return f(init)


def brute2(n):
    m = [(i1, i2, i3) for i1 in range(n) for i2 in range(i1 + 1, n) for i3 in range(i2 + 1, n)]
    init = []

    def f(vs):
        ret = 0
        if vs:
            g = Graph(n)
            for v in vs:
                (i1, i2, i3) = v
                g.addedge(i1, i2)
                g.addedge(i1, i3)
            a = g.Nconnect()
            for notv in vs:
                g = Graph(n)
                for v in vs:
                    if v == notv:
                        continue
                    (i1, i2, i3) = v
                    g.addedge(i1, i2)
                    g.addedge(i1, i3)
                if g.Nconnect() == a or (a == 1 and g.Nconnect() == 3):
                    return 0
            if a == 1:
                return 1
        ret = 0
        for v in m:
            if len(vs) == 0 or v > vs[-1]:
                ret += f(vs + [v])
        return ret
    return f(init)


def main():
    t = eval(input())
    z = [0, 1, 0, 1, 6, 25, 495, 5586, 93268, 2052513, 43258365, 1167393700, 34010847486, 1078391538159, 38595111963499, 1476893151785520, 61479081902937000, 2761923686066698561]
    for _ in range(t):
        print(z[eval(input())])


main()
