import sys
from itertools import combinations


def solve(A, x):
    if x < 0 or x > sum(A):
        return False

    sub_sum = [False] * (x + 1)
    sub_sum[0] = True
    p = 0
    while not sub_sum[x] and p < len(A):
        a = A[p]
        q = x
        while not sub_sum[x] and q >= a:
            if not sub_sum[q] and sub_sum[q - a]:
                sub_sum[q] = True
            q -= 1
        p += 1
    return sub_sum[x]


def main():
    n, w = list(map(int, sys.stdin.readline().split()))
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(w):
        val = list(map(int, sys.stdin.readline().split()))
        if val[0] == 1:
            arr[val[1] - 1] = val[2]
        elif val[0] == 2:
            a = val[1] - 1
            b = val[2]
            arr[a:b] = reversed(arr[a:b])
        else:

            if solve(arr[val[1] - 1:val[2]], val[3]):
                print("Yes")
            else:
                print("No")


main()
