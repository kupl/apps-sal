from sys import stdin, stdout
from math import floor, gcd, fabs, factorial, fmod, sqrt, inf, log
from collections import defaultdict as dd, deque
from heapq import merge, heapify, heappop, heappush, nsmallest
from bisect import bisect_left as bl, bisect_right as br, bisect
mod = pow(10, 9) + 7
mod2 = 998244353
def inp(): return stdin.readline().strip()
def out(var, end="\n"): stdout.write(str(var) + "\n")
def outa(*var, end="\n"): stdout.write(' '.join(map(str, var)) + end)
def lmp(): return list(mp())
def mp(): return map(int, inp().split())
def smp(): return map(str, inp().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]
def remadd(x, y): return 1 if x % y else 0
def ceil(a, b): return (a + b - 1) // b


def isprime(x):
    if x <= 1:
        return False
    if x in (2, 3):
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


def mergeSort(arr, n):
    temp_arr = [0] * n
    return _mergeSort(arr, temp_arr, 0, n - 1)


def _mergeSort(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += _mergeSort(arr, temp_arr,
                                left, mid)
        inv_count += _mergeSort(arr, temp_arr,
                                mid + 1, right)
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count


def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]
    return inv_count


for _ in range(int(inp())):
    n = int(inp())
    arr = lmp()
    print(mergeSort(arr, n))
