import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_int(): return list(map(int, sys.stdin.readline().strip().split()))[0]
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

N = 0
a = []

def solve():
    nonlocal N
    N = get_int()
    a = get_list()
    for i in a:
        if i == 2:
            print(1, end=' ')
        else:
            print(i ^ 2, end=' ')
    print()

test_cases = 1 # get_int()

for _ in range(test_cases):
    solve()

