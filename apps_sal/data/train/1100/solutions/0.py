"""
Input:
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains three space-separated integers p, q and r.
The second line contains three space-separated integers a, b and c.
Output:
For each test case, print a single line containing one integer ― the maximum required number of operations(if the conversion is possible), or else print "-1"
"""

T = int(input())
while T > 0:
    T -= 1
    p, q, r = list(map(int, input().split()))
    a, b, c = list(map(int, input().split()))
    s = 0
    d1 = a - p
    if d1 > 0:
        s += d1
    d2 = b - q
    if d2 > 0:
        s += d2
    d3 = c - r
    if d3 > 0:
        s += d3

    if(d1 == 0 and d2 == 0 and d3 == 0):
        print(0)
    elif(d1 < 0 or d2 < 0 or d3 < 0):
        print(-1)
    else:
        print(s)
