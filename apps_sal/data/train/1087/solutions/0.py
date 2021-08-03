#!/usr/bin/env python

def iscycle(E, v, EXPLORED_NODES, EXPLORED_EDGES):
    EXPLORED_NODES.add(v)
    r = False
    for e in [x for x in E if v in x]:
        if e in EXPLORED_EDGES:
            continue
        if e[0] == v:
            w = e[1]
        else:
            w = e[0]
        if w in EXPLORED_NODES:
            return True
        else:
            EXPLORED_EDGES.add(e)
            r = r or iscycle(E, w, EXPLORED_NODES, EXPLORED_EDGES)
            if r:
                break
    return r


def process(E):
    return iscycle(E, 1, set(), set()) and 'NO' or 'YES'


def main():
    N, M = list(map(int, input().split()))
    E = []
    for m in range(M):
        U, V = list(map(int, input().split()))
        if U > V:
            U, V = V, U
        E.append((U, V))
    print(process(E))


main()
