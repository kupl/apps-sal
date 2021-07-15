n = int(input())
a = input() + '$'
b = input() + '$'
weight = 0
i = 0
while i < n:
    if a[i] != b[i]:
        weight += 1
        if a[i] == b[i + 1] and a[i + 1] == b[i]:
            i += 2
            continue
    i += 1
print(weight)
