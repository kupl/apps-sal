# cook your dish here
# code by RAJ BHAVSAR
import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_print_int(x): sys.stdout.write(str(x) + '\n')
def get_print(x): sys.stdout.write(x + '\n')


def solve():
    for _ in range(get_int()):
        s = get_string()
        n = len(s)
        count = 0
        for i in s:
            if(i == 'a'):
                count += 1
        get_print_int((2**n - 1) - (2**(n - count) - 1))


solve()
