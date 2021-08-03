# cook your dish here
n = int(input())
arr = list(map(int, input().split()))
dr = {}
for i in arr:
    if i in dr.keys():
        dr[i] += 1
    else:
        dr[i] = 1
ct = 0
for i in dr.keys():
    if dr[i] % 2 == 0:
        ct += dr[i] // 2
    else:
        ct += (dr[i] // 2 + 1)
print(ct)
