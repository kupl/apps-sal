n = int(input())
dictt = {}
arr = []
for i in range(n):
    a = input()
    arr.append(a)
for i in range(0, n):
    for j in range(0, 7):
        if arr[i][j] == '1':
            try:
                dictt[j] += 1
            except:
                dictt[j] = 1
try:
    print(max(dictt.values()))
except:
    print(0)
