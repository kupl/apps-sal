from collections import Counter

class FastScanner:
    def __init__(self):
        import sys
        self.inp = sys.stdin.read().split()
        self.readAt = -1
    def nextInt(self):
        self.readAt += 1
        return int(self.inp[self.readAt])
    def nextString(self):
        self.readAt += 1
        return self.inp[self.readAt]
    def nextRange(self, n):
        self.readAt += n
        return self.inp[self.readAt-n+1:self.readAt+1]
    def skip(self, n):
        self.readAt += n
 
class PrintWriter:
    def __init__(self):
        self.pw = []
    def println(self, n):
        self.pw.append(n)
    def flush(self):
        print("\n".join(map(str, self.pw)))
        self.pw = []

class Factorial:
    def __init__(self, limit, MOD):
        self.fac = [1]
        for i in range(1, limit+1):
            self.fac.append((i*self.fac[-1]) % MOD)
    def __getitem__(self, n):
        return self.fac[n]

def modInverse(n, p):
    return pow(n, p-2, p)

def nCr(n, r, f, MOD):
    if r>n: return 0
    x = f[n] % MOD
    y = f[r] % MOD
    z = f[n-r] % MOD
    return (x * modInverse(y, MOD) * modInverse(z, MOD)) % MOD

def main():
    MOD = 1000000007
    limit = 100000
    fs = FastScanner()
    pw = PrintWriter()
    f = Factorial(limit, MOD)
    t = fs.nextInt()
    for i in range(t):
        A = fs.nextString()
        n = len(A)
        mapp = Counter(A)
        combs = f[n]
        sim2 = nCr(n, 2, f, MOD)
        sim3 = nCr(n, 3, f, MOD)
        sim4 = nCr(n, 4, f, MOD) * 3
        nm2c2 = nCr(n-2, 2, f, MOD)
        for i in mapp:
            combs = (combs * modInverse(f[mapp[i]], MOD)) % MOD
            ncr2 = nCr(mapp[i], 2, f, MOD)
            rest = n - mapp[i]
            sim2 -= ncr2
            sim3 -= ncr2*rest
            sim4 -= ((nm2c2 * ncr2) % MOD)
            ncr3 = nCr(mapp[i], 3, f, MOD)
            sim3 -= ncr3
            ncr4 = nCr(mapp[i], 4, f, MOD)
            sim4 += ((ncr4 * 3) % MOD)
        summ = ((combs * (combs-1)) % MOD)
        sim2 = ((combs * sim2 * 1) % MOD)
        sim3 = ((combs * sim3 * 2) % MOD)
        sim4 = ((combs * sim4) % MOD)
        pw.println((summ - (sim2 + sim3 + sim4)) % MOD)
    pw.flush()

def __starting_point():
    main()

__starting_point()
