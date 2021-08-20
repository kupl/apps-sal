n = int(input())
l = list(input())
j = 0
count = 0
while j < len(l) - 1:
    if l[j] == l[j + 1]:
        j -= 1
        count += 1
        l.pop(j + 1)
    j += 1
print(count)
