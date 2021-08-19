# cook your dish here
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    atomlist = [''] * n
    for k in range(m):
        s = []
        s.extend(input().split()[1:])
        # print(s)
        for w in range(n):
            if str(w) in s:
                atomlist[w] += "1"
            else:
                atomlist[w] += "0"
        # print(atomlist)
    print(len(set(atomlist)))
