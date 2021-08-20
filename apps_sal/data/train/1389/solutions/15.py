n = int(input())
arr = []
d = ["'", '.', ',', ';', ':']
for i in range(n):
    temp = input().strip()
    for j in d:
        if j in temp:
            temp = temp.replace(j, '')
    temp = temp.split()
    temp.reverse()
    arr.append(temp)
for i in range(len(arr) - 1, -1, -1):
    print(' '.join(arr[i]))
