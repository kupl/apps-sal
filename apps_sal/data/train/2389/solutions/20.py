import sys
 
t = int(input())
for _ in range(t):
    n, k = list(map(int, sys.stdin.readline().split()))
    s = sys.stdin.readline()
    d = {}
    d['R'] = [0,0,0]
    d['G'] = [0,0,0]
    d['B'] = [0,0,0]
    res = 0
    for i in range(k):
        d[s[i]][i%3] += 1
    res = max(d['R'][0] + d['G'][1] + d['B'][2], d['R'][1] + d['G'][2] + d['B'][0], d['R'][2] + d['G'][0] + d['B'][1])
    for i in range(k, n):
        d[s[i]][i%3] += 1
        d[s[i-k]][(i-k)%3] -= 1
        res = max(res, d['R'][0] + d['G'][1] + d['B'][2], d['R'][1] + d['G'][2] + d['B'][0], d['R'][2] + d['G'][0] + d['B'][1])
        if res >= k:
            break
    print(k-res)
        


