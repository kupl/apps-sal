s = input()
n = int(input())
a = [input() for i in range(n)]
for x in a:
    for y in a:
        if s in x + y:
            print('YES')
            return

print('NO')
