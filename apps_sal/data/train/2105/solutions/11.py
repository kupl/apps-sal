import sys

fin = sys.stdin
fout = sys.stdout
n = int(fin.readline())
colors = [1] * n
allCount = 1
for i in range(2, n + 2):
    if colors[i - 2] == 1 and i * i <= n + 1:
        allCount += 1
        for j in range(i * i, n + 2, i):
            colors[j - 2] = 2
fout.write(str(max(colors)) + '\n')
fout.write(' '.join(map(str, colors)))
