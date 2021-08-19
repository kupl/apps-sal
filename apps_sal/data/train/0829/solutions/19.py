# cook your dish here
N = int(input())
l = list(map(int, input().strip().split(" ")))
s = 0
for i in range(N):
    for j in range(i + 1, N):
        s += abs(l[j] - l[i])
print(s)


"""
l.sort()

s = 0
for i in range(len(l)):
    s -= (len(l) - i - 1) * l[i]
    s += i * l[i]
print(s)
"""
