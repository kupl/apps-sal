arr = []
for a in range(int(input())):
    b = list(input())
    if '4' in b:
        arr.append(b.count('4'))
    else:
        arr.append(0)
print(*arr, sep='\n')
