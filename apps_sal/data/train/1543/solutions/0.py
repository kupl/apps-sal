for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    atomlist = [''] * n
    for k in range(m):
        s = []
        s.extend(input().split()[1:])
        for w in range(n):
            if str(w) in s:
                atomlist[w] += '1'
            else:
                atomlist[w] += '0'
    print(len(set(atomlist)))
