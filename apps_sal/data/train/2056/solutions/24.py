import sys
input = sys.stdin.readline
n = int(input())
a = input()
b = input()
s = 0
i = 0
while i != len(a):
    if a[i] != b[i]:
        if a[i + 1] != b[i + 1] and a[i] != a[i + 1]:
            s += 1
            i += 2
        else:
            s += 1
            i += 1
    else:
        i += 1
print(s)
