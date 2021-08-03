import sys
for _ in range(0, eval(input())):
    d, inp, mp, n, q = set(), list(map(ord, list(sys.stdin.readline().strip()))), [x == 'g' for x in list(sys.stdin.readline().strip())], eval(input()), ord('a')
    for i in range(0, len(inp)):
        nn, h = n, 0
        for j in range(i, len(inp)):
            if ((mp[inp[j] - q]) or nn > 0):
                if(mp[inp[j] - q] == False):
                    nn = nn - 1
                h = (h * 128) ^ inp[j]
                d.add(h)
            else:
                break
    print(len(d))
