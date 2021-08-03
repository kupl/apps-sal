main = list([int(x) for x in input().split()])
n, l = main[0], main[1]
final = []
for i in range(n):
    string = input()
    final.append(string)

final.sort()
print((''.join(final)))
