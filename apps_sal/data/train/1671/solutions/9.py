from sys import stdin, stdout
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    # a=list(map(int,stdin.readline().split()))
    a = [1] * n
    print(*a)
