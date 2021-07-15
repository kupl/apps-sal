#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout

from itertools import repeat
from heapq import nlargest
from operator import itemgetter

class bag(dict):

    def __init__(self, data=()):
        self.update(data)

    def __missing__(self, key):
        return 0

    def update(self, other):
        if hasattr(other, 'items'):
            super(bag, self).update(other)
        else:
            for elem in other:
                self[elem] += 1

    def __setitem__(self, elem, n):
        if n <= 0:
            if elem in self:
                del self[elem]
        else:
            super(bag, self).__setitem__(elem, n)

    def itermultiple(self):
        for elem, cnt in self.items():
            for _ in range(cnt):
                yield elem

    def nitems(self):
        return sum(self.values())

    def most_common(self, n=None):
        if n is None:
            return sorted(iter(self.items()), key=itemgetter(1), reverse=True)
        else:
            return nlargest(n, iter(self.items()), key=itemgetter(1))

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, dict.__repr__(self))

    def add(self, item, n=1):
        self[item] += n

    def discard(self, item, n=1):
        self[item] -= n


def solve(A):
    C = bag(A)
    MC = C.most_common()
    e,c = MC.pop(0)
    c_max = c
    e_min = e
    for mc in MC:
        e,c = mc
        if c==c_max:
            if e < e_min:
                e_min = e
        else:
            break
    return (e_min,c_max)


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d) if len(s.strip())>0]


T = int(ifs.readline())
for t in range(1,T+1):
    n = int(ifs.readline())
    A = numbers_from_line()
    v,c = solve(A)
    ofs.write('%d %d\n' % (v,c))


sys.exit(0)

