from sys import stdin, stdout
# #from collections import Counter
# n = int(stdin.readline())
# #l = list(map(int, stdin.readline().split()))
# #l = [int(stdin.readline()) for _ in range(n)]
# #a, b = input().split()
# for _ in range(n):
n1 = int(stdin.readline())
l = list(map(int, stdin.readline().split()))
for x in l:
    if x != 2:
        print(x ^ 2, end=' ')
    else:
        print(1, end=' ')
print()
