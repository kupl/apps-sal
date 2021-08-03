

def solve():
    #n, m = [int(i) for i in input().split(' ')]
    n = int(input())
    a = [int(i) for i in input().split(' ')]
    a.sort()
    md = 10000
    for i in range(n - 1):
        md = min(a[i + 1] - a[i], md)

    return md


for t in range(int(input())):
    print(solve())
