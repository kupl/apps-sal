# cook your dish here
"""
At first when you look at the problem you nitice that it may be a depth search     problem
so you made a column and row number form yourself and readlised that all     diagonals
add to one.

so the total number of diagonals will be a+b-1

for 3*4 matrix

1         0.5       0.25              0.125
0.5       0.5       0.375             0.375/2 + 0.125
0.25      0.5       0.375/2+0.5       1

use depth search approach to get the individual probability 
"""

testcase = int(eval(input()))
for z in range(testcase):
    a, b = [int(d) for d in input().split()]
    print(a + b - 1)
