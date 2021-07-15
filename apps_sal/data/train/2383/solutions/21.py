from sys import stdin

inp = lambda: stdin.readline().strip()

t = int(inp())

for _ in range(t):
     a, b = [int(x) for x in inp().split()]
     minimum = min(a,b)
     maximum = max(a,b)
     print(max(maximum,2*minimum)**2)

