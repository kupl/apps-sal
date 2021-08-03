import sys
for _ in range(0, eval(input())):
    d, ctr, inp, mp, n, q = [0] * 4000000, 0, list(map(ord, list(sys.stdin.readline().strip()))), sys.stdin.readline().strip(), eval(input()), ord('a')
    for i in range(0, len(inp)):
        nn, h = n, 0
        for j in range(i, len(inp)):
            if ((mp[inp[j] - q] == 'g') or nn > 0):
                if((mp[inp[j] - q] == 'g') == False):
                    nn = nn - 1
                h = (h * 128) ^ inp[j]
                d[ctr], ctr = h, ctr + 1
            else:
                break
    d = d[0:ctr]
    print(len(set(d)))
