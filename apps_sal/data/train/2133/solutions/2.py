n = int(input())
w = [0, 0, 0, 0, 0, 0, 0]
for i in range(n):
    j = 0
    for i in input():
        if i == '1':
            w[j] += 1
        j += 1
print(max(w))
