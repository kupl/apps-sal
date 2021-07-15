t = int(input())
names = 'Dee', 'Dum'
for _ in range(t):
 n, s = input().split()
 n = int(n)
 c = [0, 0]
 for _ in range(n):
  b = list(map(int, input()))
  c[b[0]] += b.count(b[0])
 print(names[c[0] == c[1] and s == 'Dee' or c[0] < c[1]])

