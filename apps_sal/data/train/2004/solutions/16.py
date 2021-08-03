n = (input())
i = 0
while i < len(n) - 1 and n[i] != '0':
    print(n[i], end='')
    i += 1
if n[i] == '0':
    j = i + 1
    while j < len(n):
        print(n[j], end='')
        j += 1
