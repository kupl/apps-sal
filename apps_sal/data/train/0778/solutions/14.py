arr = []
for a in range(int(input())):
    arr.append(int("".join(reversed(input()))))
print(*arr, sep='\n')
