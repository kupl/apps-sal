# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.readline
#from heapq import heappop, heappush
from collections import defaultdict
#from itertools import combinations
sys.setrecursionlimit(10**7)
import math
class SegTree():
    '''
    input idx: 1-
    '''
    def __init__(self, n, init_val=0):
        self.n = n
        self.init_val = init_val
        self.n_leaf = 2 ** math.ceil(math.log2(n))
        self.bins = [init_val] * (self.n_leaf * 2)

    def val_append(self, A):
        '''
        :param A:
        :return:
        '''
        if len(A) != self.n:
            raise ValueError('The number of input should be same with n_leaf')
        for i,a in enumerate(A):
            self.bins[self.n_leaf+i]=a
        self._calc()
        return None

    def _calc(self):
        '''
        Calculate all bins based on values of leaves
        '''
        i = self.n_leaf - 1
        while i > 0:
            self.bins[i] = self._criteria(self.bins[i*2], self.bins[i*2+1])
            i -= 1
        return None

    def _criteria(self, x, y):
        '''
        Define criteria between 2 nodes
        '''
        return x | y

    def eval_between(self, x, y):
        '''
        x, y : node-idx(1-)
        '''
        l, r = x + self.n_leaf - 1, y + self.n_leaf - 1
        ret = self._criteria(self.bins[l], self.bins[r])
        while l < r:
            if l % 2 == 1:
                ret = self._criteria(self.bins[l], ret)
                l += 1
                continue

            if r % 2 == 0:
                ret = self._criteria(self.bins[r], ret)
                r -= 1
                continue
            l = l//2
            r = r//2
            ret = self._criteria(self.bins[l], ret)
            ret = self._criteria(self.bins[r], ret)

        return ret

    def update(self, node, pro):
        '''
        Replacement of the value in a leaf
        '''
        current = node + self.n_leaf - 1
        self.bins[current] = pro
        current //= 2
        while current > 0:
            self.bins[current] = self._criteria(self.bins[current*2+1], self.bins[current*2])
            current //= 2
        return None

def run():
    N = int(input())
    S = list(input())
    Q = int(input())
    queries = [sysread().split() for _ in range(Q)]

    bins = [0] * N# a: ord('a') - 97
    for i,s in enumerate(S):
        id = ord(s) - 97
        bins[i] = 1<<id

    segtree = SegTree(N)
    segtree.val_append(bins)

    for type, i,c in queries:
        if type == '1':
            c = 1 << (ord(c) - 97)
            segtree.update(int(i), c)
        else:
            i,c = int(i), int(c)
            tmp = segtree.eval_between(i,c)
            print(bin(tmp).count('1'))

def __starting_point():
    run()
__starting_point()
