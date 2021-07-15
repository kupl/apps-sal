input()
a = [int(x) for x in input().split()]

lowest = a[0]
lowests = {a[0]}
diff = -1
pairs = []

for x in a[1:]:
    if lowest > x:
        lowests = {x}
        lowest = x
    elif lowest == x:
        lowests.add(x)
    elif diff == x - lowest:
        pairs += [(x, y) for y in lowests]
    elif diff < x - lowest:
        pairs = [(x, y) for y in lowests]
        diff = x - lowest

a, b = list(zip(*pairs))
print((min(len(set(a)), len(set(b)))))

