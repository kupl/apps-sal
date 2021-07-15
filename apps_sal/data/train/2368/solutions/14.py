#Bhargey Mehta (Junior)
#DA-IICT, Gandhinagar
import sys, math
mod = 10**9

def solve(test_index):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    tga, tgb = min(a), min(b)
    ans = 0
    for i in range(n):
        ans += max(a[i]-tga, b[i]-tgb)
    print(ans)
    return

if 'PyPy' not in sys.version:
    sys.stdin = open('input.txt', 'r')

sys.setrecursionlimit(100000)
num_tests = 1
num_tests = int(input())
for test in range(1, num_tests+1):
    #print("Case #{}: ".format(test), end="")
    solve(test)
