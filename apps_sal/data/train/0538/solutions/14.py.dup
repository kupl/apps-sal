# cook your dish here
from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    spd, sg, fg, d, time = map(int, stdin.readline().split())
    ckh = ((d * 180) / time) + spd
    dsg = abs(ckh - sg)
    dfg = abs(ckh - fg)
    ans.append('DRAW' if dsg == dfg else 'SEBI' if dsg < dfg else 'FATHER')
stdout.write('\n'.join(ans))
