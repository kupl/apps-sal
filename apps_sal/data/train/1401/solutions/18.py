# cook your dish here
n, k = list(map(int, input().split()))
arr = [int(i) for i in input().split()]
arr.sort()
x = 0
l = []
for i in arr:
    x += i
    if x <= k:
        l.append(i)
print(len(l))
