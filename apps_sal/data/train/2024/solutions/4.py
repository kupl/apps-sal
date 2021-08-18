n = input()

read = input()

p = []

for x in read.split():

    p.append((float)(x))


v = 0.0

l = 0.0

for u in p:

    v = v * (1 - u) + u * (v + 2 * l + 1)

    l = (l + 1) * u

print(v)
