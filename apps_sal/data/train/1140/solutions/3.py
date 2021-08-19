# cook your dish here
t = input()
for i in range(int(t)):
    inp = input()
    p, idx = int(inp.split()[0]), inp.split()[1]
    binidxlist = [i for i in bin(int(idx))[2:]]
    binidx = ""
    for j in binidxlist:
        binidx += j
    binidx = int(binidx[::-1] + ("0" * (p - len(binidx))), 2)
    print(binidx)
