alphabet = 'abcdefghijklmnopqrstuvwxyz'


def recursion(s, start, end, height):
    if end - start == 1:
        if s[start] == alphabet[height]:
            return 0
        else:
            return 1
    else:
        middle = (start + end) // 2
        return min(
            recursion(s, middle, end, height + 1) + (end - start) // 2 - s[start:middle].count(alphabet[height]),
            recursion(s, start, middle, height + 1) + (end - start) // 2 - s[middle:end].count(alphabet[height]),
        )


def solve():
    n = int(input())
    s = input()
    print(recursion(s, 0, n, 0))


for _ in range(int(input())):
    solve()

