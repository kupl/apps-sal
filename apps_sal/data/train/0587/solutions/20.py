from sys import stdin, stdout
n1 = int(stdin.readline())
l = list(map(int, stdin.readline().split()))
for x in l:
    if x != 2:
        print(x ^ 2, end=' ')
    else:
        print(1, end=' ')
print()
