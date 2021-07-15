import queue
n, a, b = list(map(int, input().split()))
x = list(map(int, input().split()))

vals = [float('inf')]*n
vals[0] = 0

c = queue.Queue()
c.put(1)

while not c.empty():
    d = c.get()
    if d == n:
        continue
    if b+vals[d-1] < vals[d]:
        vals[d] = b+vals[d-1]
    if a*(x[d]-x[d-1])+vals[d-1] < vals[d]:
        vals[d] = a*(x[d]-x[d-1])+vals[d-1]
    c.put(d+1)
print((vals[-1]))

