t = int(input())
for _ in range(t):
    n, s = input().split()
    n = int(n)
    c = [0, s == 'Dee']
    for _ in range(n):
        b = input()
        c[b[0] == '1'] += b.count(b[0])
    print(('Dee', 'Dum')[c[0] < c[1]])
