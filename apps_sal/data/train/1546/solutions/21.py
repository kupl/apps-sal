

import sys


def main():
    def checkValidity(a, b, c):
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            return False
        else:
            return True

    def checkrt(a, b, c):
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return True
        return False
    for tc in range(int(input())):
        a, b, c = get_ints()
        if checkValidity(a, b, c):
            if checkrt(a, b, c):
                print('YES')
            else:
                print('NO')
        else:
            print('NO')


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return list(map(int, sys.stdin.readline().split()))


def input(): return sys.stdin.readline().strip()


main()
