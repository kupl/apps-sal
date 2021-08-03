#! /usr/bin/python

t = int(input())

for i in range(t):
    inp = input().split()
    a = list(inp[0])
    b = list(inp[1])

    a.reverse()
    b.reverse()

    x = int(''.join(a))
    y = int(''.join(b))

    c = list(str(x + y))
    c.reverse()

    z = int(''.join(c))
    print(z)
