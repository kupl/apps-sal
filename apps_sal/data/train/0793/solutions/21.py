from sys import stdin, stdout
import bisect
from collections import defaultdict


def main():
    (n, d) = map(int, stdin.readline().split())
    arr = [int(k) for k in stdin.readline().split()]
    arr.sort()
    ind = bisect.bisect_left(arr, d)
    diff = -1
    if ind != n and arr[ind] == d:
        if ind == n - 1:
            diff = abs(arr[ind - 1] - d)
        else:
            diff = min(abs(arr[ind + 1] - d), abs(arr[ind - 1] - d))
    elif ind == n:
        diff = abs(arr[ind - 1] - d)
    else:
        diff = abs(arr[ind] - d)
    counter = 0
    for i in range(1, n):
        if abs(arr[i] - arr[i - 1]) % diff != 0:
            counter = 1
            break
    if counter == 1:
        print(1)
    else:
        print(diff)


def __starting_point():
    main()


__starting_point()
