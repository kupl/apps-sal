class Dsu:
    def __init__(self, v, s):
        self.par = s
        self.v = v
        self.dr = [1] * v
        self.zero = [False] * v
        self.speed = []
        for i in range(v):
            self.speed.append([])
            self.speed[i].append(i)

    def find(self, i):
        if i != self.par[i][0]:
            org = self.par[i][0]
            self.par[i][0] = self.find(self.par[i][0])
            if self.zero[i] or self.zero[self.par[i][0]] or self.zero[org]:
                self.zero[i] = self.zero[self.par[i][0]] = self.zero[org] = True
            if org != self.par[i][0]:
                self.speed[self.par[i][0]].append(i)
        return self.par[i][0]

    def union(self, x, y):
        self.rx = self.find(x)
        self.ry = self.find(y)
        self.sign = -self.dr[x] * self.dr[y]
        if self.rx != self.ry:
            if (self.par[self.rx][1] < self.par[self.ry][1]):
                mx = self.ry
                mn = self.rx
            if (self.par[self.rx][1] > self.par[self.ry][1]):
                mx = self.rx
                mn = self.ry
            if self.par[self.rx][1] != self.par[self.ry][1]:
                self.par[mn][0] = mx
                if self.zero[mn] or self.zero[mx] or self.zero[x] or self.zero[y]:
                    self.zero[mn] = self.zero[mx] = self.zero[x] = self.zero[y] = True
                else:
                    for i in range(len(self.speed[mn])):
                        self.dr[self.speed[mn][i]] *= self.sign
                        org = self.par[self.speed[mn][i]][0]
                        if org != mx:
                            self.par[self.speed[mn][i]][0] = mx
                            self.speed[mx].append(self.speed[mn][i])
                self.speed[mx].append(mn)

            else:
                self.par[self.ry][0] = self.rx
                self.par[self.rx][1] += 1
                if self.zero[self.rx] or self.zero[self.ry] or self.zero[x] or self.zero[y]:
                    self.zero[self.rx] = self.zero[self.ry] = self.zero[x] = self.zero[y] = True
                else:
                    for i in range(len(self.speed[self.ry])):
                        self.dr[self.speed[self.ry][i]] *= self.sign
                        org = self.par[self.speed[self.ry][i]][0]
                        if org != self.rx:
                            self.par[self.speed[self.ry][i]][0] = self.rx
                            self.speed[self.rx].append(self.speed[self.ry][i])
                self.speed[self.rx].append(self.ry)
        else:
            return


def optwo(x, y, D):
    if (D.find(x) == D.find(y) and D.dr[x] == D.dr[y]):
        D.zero[x] = D.zero[y] = True
    D.union(x, y)


def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)


def opthree(x, y, v, D):
    if (D.find(x) != D.find(y)) or (D.zero[D.par[y][0]]):
        print(0)
    else:
        g = gcd(v * speed[x], speed[y])
        flag = (D.dr[x] * D.dr[y]) // abs(D.dr[x] * D.dr[y])
        print(str(flag * v * speed[x] // g) + "/" + str(speed[y] // g))


n, M = map(int, input().split())
speed = list(map(int, input().split()))
s = []
for i in range(n):
    s.append([i, 0])
D = Dsu(n, s)
for i in range(M):
    T = list(map(int, input().split()))
    if (T[0] == 1):
        speed[T[1] - 1] = T[2]
    elif (T[0] == 2):
        optwo(T[1] - 1, T[2] - 1, D)
    elif (T[0] == 3):
        opthree(T[1] - 1, T[2] - 1, T[3], D)
