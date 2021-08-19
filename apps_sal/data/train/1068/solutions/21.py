# cook your dish here

def isOdd(n):
    return True if n % 2 != 0 else False


def isPossible(a, b):
    return "NO" if isOdd(a) and isOdd(b) else "YES"


def __starting_point():
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        print(isPossible(a, b))


__starting_point()
