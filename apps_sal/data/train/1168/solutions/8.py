import sys
for _ in range(0, eval(input())):
    (d, c, inp, mp, n) = ([], 0, sys.stdin.readline().strip(), sys.stdin.readline().strip(), eval(input()))
    for i in range(0, len(inp)):
        (nn, h) = (n, 0)
        for j in range(i, len(inp)):
            if mp[ord(inp[j]) - ord('a')] == 'g' or nn > 0:
                if (mp[ord(inp[j]) - ord('a')] == 'g') == False:
                    nn = nn - 1
                h = h * 256 ^ ord(inp[j])
                d += [h]
            else:
                break
    print(len(set(d)))
