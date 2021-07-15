import sys
def calc(b0, b1, q):
    if q == 0:
        return b0 ^ b1
    if q == 1:
        return b0 | b1
    if q == 2:
        return b0 & b1
n, m = list(map(int,sys.stdin.readline().split()))
arr1 = {}
opt = ['XOR', 'OR', 'AND']
arr2 = []
for j in range(n):
    a, b = list(map(str,sys.stdin.readline().split(" := ")))
    b = b.split()
    if len(b) == 1:
        s = b[0]
        arr1[a] = s
    else:
        c = b[0]
        d = b[2]
        q = opt.index(b[1])
        arr2.append((a, c, d, q))
 
mins = ''
maxs = ''
d0 = {'?':0}
d1 = {'?':1}
for i in range(m):
    for a, b in list(arr1.items()):
        d0[a] = int(b[i])
        d1[a] = int(b[i])
    s0 = 0
    s1 = 0
    for a, c, d, q in arr2:
        b00 = d0[c]
        b01 = d0[d]
        b10 = d1[c]
        b11 = d1[d]
        c0 = calc(b00, b01, q)
        c1 = calc(b10, b11, q)
        s0 += (1 if c0 else 0)
        s1 += (1 if c1 else 0)
        d0[a] = c0
        d1[a] = c1
    if s1 < s0:
        mins += "1"
    else:
        mins += "0"
    if s1 > s0:
        maxs += "1"
    else:
        maxs += "0"
sys.stdout.write("{0}\n{1}".format(mins,maxs))



    


