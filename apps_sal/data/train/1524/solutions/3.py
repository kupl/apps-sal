# your code goes here
import sys
t = eval(input())
for i in range(0, t):
    a, b = list(map(int, sys.stdin.readline().split(' ')))
    if(b == 1):
        print(0)
    else:
        ans = b * ((b - 1)**(a - 1)) % 1000000007
        print(ans)
