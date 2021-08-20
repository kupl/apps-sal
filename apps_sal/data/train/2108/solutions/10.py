import sys
fin = sys.stdin
fout = sys.stdout
cur = fin.readline().split()
n = int(fin.readline())
fout.write(' '.join(cur) + '\n')
for i in range(n):
    curS = fin.readline().split()
    pos = cur.index(curS[0])
    cur[pos] = curS[1]
    fout.write(' '.join(cur) + '\n')
