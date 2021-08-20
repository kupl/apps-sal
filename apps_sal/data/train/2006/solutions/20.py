import math
n = int(input())
arr = list(map(int, input().split()))
gcd = 0
for num in arr:
    gcd = math.gcd(gcd, num)
moves = max(arr) / gcd - n
if moves % 2:
    print('Alice')
else:
    print('Bob')
