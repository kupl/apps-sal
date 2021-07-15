s = input()
n = int(input())
a = [input() for i in range(n)]
for i in a:
    for j in a:
        if s in i + j:
            print('YES')
            return
print('NO')

