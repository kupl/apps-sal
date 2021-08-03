n, l = map(int, input().split())
str = [input() for i in range(n)]
str.sort()
for i in str:
    print(i, end='')
