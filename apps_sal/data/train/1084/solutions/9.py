# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

s = input()
arr = []
n = len(s)
i = 0

while (i < n):
    x = s[i]
    while (i < n and s[i] == x):
        i += 1
    arr.append(x)

m = len(arr)
if (arr[0] == "0"):
    if (m == 1):
        print(0)
    else:
        print((m // 2) * 2)
else:
    if (m & 1 == 1):
        print((m // 2) * 2 + 1)
    else:
        m -= 1
        print((m // 2) * 2 + 1)
