# cook your dish here
n = int(input())
l = list(map(int, input().split()))[:n]
d = {}
for i in l:
    d[i] = d.get(i, 0) + 1
s = 0
for key, value in d.items():
    s += (value // 2) + (value % 2)
print(s)
