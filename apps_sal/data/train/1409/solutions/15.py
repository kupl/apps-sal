import sys
input = sys.stdin.readline

try:
    for _ in range(int(input())):
        n = int(input())
        ans = 0
        while n:
            if n & 1:
                ans += 1
            n = n // 2
        print(ans)


except EOFError as e:
    print(e)
