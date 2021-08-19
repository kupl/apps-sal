# n,k = map(int,input().strip().split(" ")) takes two number as input in a     single line
# arr = list(map(int,input().split())) takes an array as a input in a single     line
# arr = [int(input()) for i in range(n)] takes an array as input in different     lines

def solve():
    n = int(input())
    sr = input()
    print(min(sr))


t = int(input())
while t > 0:
    solve()
    t -= 1
