import sys
mod = 1000000007
def get_array(): return list(map(int, sys.stdin.readline().split()))
def get_ints(): return map(int, sys.stdin.readline().split())
def input(): return sys.stdin.readline()
def print_array(a): print(" ".join(map(str, a)))


def main():
    for _ in range(int(input())):
        n = int(input())
        a = get_array()
        m = a[n - 1]
        cnt = 0
        for i in range(n - 2, -1, -1):
            if a[i] > m:
                cnt += 1
            if a[i] < m:
                m = a[i]
        print(cnt)


def __starting_point():
    main()


__starting_point()
