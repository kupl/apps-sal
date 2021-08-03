"""
-----------------------------Pseudo---------------------------------
"""
import copy
import sys
from collections import defaultdict, Counter


def input(): return sys.stdin.readline()
def mapi(): return map(int, input().split())
def maps(): return map(str, input().split())
#


def print(arg, *argv, end=None):
    sys.stdout.write(str(arg))
    for i in argv:
        sys.stdout.write(" " + str(i))
    sys.stdout.write(end) if end else sys.stdout.write("\n")

#---------------------------------------------------------------#


mod = 1000000007


class Matrix(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.mat = [[0] * cols for i in range(rows)]

    def __len__(self):
        return len(self.mat)

    def __getitem__(self, key1):
        return self.mat[key1]

    def __setitem__(self, key1, value):
        self.mat[key1] = value

    def __str__(self):
        res = ""
        for i in self.mat:
            res += " ".join(str(j) for j in i) + "\n"
        return res[:-1]

    def __mul__(self, other):
        if len(other) != len(self.mat[0]):
            print("matrices are not compitable for multiplication")
            return
        res = Matrix(len(self.mat), len(other[0]))
        for i in range(self.rows):
            for j in range(len(other[0])):
                ans = 0
                for k in range(len(other)):
                    ans += self.mat[i][k] * other[k][j] % mod
                res[i][j] = ans % mod
        return res
    """
    def __pow__(self, n):
     if n==0 or n==1:
      return self
     tmp = self
     #copy.deepcopy(self)
     tmp = tmp**(n//2)
     #print(tmp)
     tmp = tmp*tmp
     if(n%2 != 0):
      tmp = tmp*self
     return tmp
    """

    def __pow__(self, n):
        res = Matrix(self.rows, self.rows)
        tmp = self
        for i in range(self.rows):
            res[i][i] = 1
        while n > 0:
            if n & 1:
                res = res * tmp
            n >>= 1
            tmp = tmp * tmp
        return res


"""
dp[1] = m
dp[2] = m^2
dp[3] = m^3-m
recurrent relation:  dp[i] = m*dp[i-1] - (m-1)*dp[i-3]

"""


def solve():
    t = 1
    t = int(input())
    while(t):
        t -= 1
        n, m = mapi()
        m %= mod
        B = Matrix(3, 1)
        M = Matrix(3, 3)
        B[0][0] = m
        B[1][0] = (m * m) % mod
        B[2][0] = ((m * m % mod + mod - 1) % mod) * m % mod

        M[0][1] = 1
        M[1][2] = 1
        M[2][0] = (mod - m + 1) % mod
        M[2][1] = 0
        M[2][2] = m
        # print(M)
        M = M**(n - 1)
        B = M * B
        # print(B)
        print(B[0][0])

#---------------------------------------------------------------#


def __starting_point():
    solve()


__starting_point()
