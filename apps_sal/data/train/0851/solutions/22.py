from sys import stdin
# t = int(input())
# nks = stdin.readlines()
# print(nks)
for _ in range(int(input())):
    n,k = [int(x) for x in input().split()]
    # n,k = [int(x) for x in line.split()]
    ans = (1 + n*(k-1))/k
    print(ans*2)
