"""
Name : Jaymeet Mehta
codechef id :mj_13
Problem : Triangle love part 2 
"""
from sys import stdin, stdout


def calc(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    if b ** 2 + c ** 2 == a ** 2:
        return True
    if a ** 2 + c ** 2 == b ** 2:
        return True
    return False


test = int(stdin.readline())
for _ in range(test):
    (a, b, c) = map(int, stdin.readline().split())
    if a == 0 or b == 0 or c == 0:
        print('NO')
        continue
    print('YES') if calc(a, b, c) else print('NO')
