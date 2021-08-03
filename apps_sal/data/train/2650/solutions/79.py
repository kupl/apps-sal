# -*- coding: utf-8 -*-

n, l = map(int, input().split())
s = [input() for i in range(n)]
s = sorted(s)
print(*s, sep="")
