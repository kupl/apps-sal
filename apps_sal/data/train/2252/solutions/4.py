from collections import Counter

n = int(input())
strings = []

for i in range(0, n):
    counter = {x: 0 for x in range(ord('a'), ord('z') + 1)}
    napis = input()
    for val in napis:
        counter[ord(val)] = (counter[ord(val)] + 1) % 2

    napis = ""
    for key, val in list(counter.items()):
        if val != 0:
            napis += chr(key)

    strings.append(napis)

c = Counter(strings)
strings = sorted(c.most_common(), key=lambda i: i[0])

count = 0
for key, val in strings:
    if val > 1:
        count += val * (val - 1) / 2

for charInt in range(ord('a'), ord('z') + 1):
    char = chr(charInt)
    copy = {}
    for key, val in strings:
        if char in key:
            copy[key.replace(char, "")] = copy.get(key.replace(char, ""), 0) + val
    for key, val in strings:
        if copy.get(key, 0) != 0:
            count += val * copy[key]

print(int(count))
