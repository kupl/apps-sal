import sys
input = sys.stdin.readline

n, q = list(map(int, input().split()))
for i in range(q):
    a = int(input())
    if a % 2 != 0:
        print((a + 1) // 2)
    else:
        b = a // 2
        while 1 > 0:
            a = a + (n - b)
            b = a // 2
            if a % 2 != 0:
                print((a + 1) // 2)
                break
