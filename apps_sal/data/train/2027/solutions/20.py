s = input()
pos1 = []
pos2 = []
n = len(s)
for i in range(n):
    if s[i] == 'l':
        pos2.append(i + 1)
    else:
        pos1.append(i + 1)
for i in pos1:
    print(i)
for i in pos2[::-1]:
    print(i)
