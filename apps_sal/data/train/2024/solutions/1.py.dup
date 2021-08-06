n = input()
read = input()
p = []
for x in read.split():
    p.append((float)(x))

v = 0.0
l = 0.0
for item in p:
    v = v * (1 - item) + item * (v + 2 * l + 1)
    l = (l + 1) * item
print(v)
