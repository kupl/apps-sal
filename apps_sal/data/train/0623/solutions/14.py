n = int(input())
array = []
for i in range(n):
    k = int(input())
    array.append(k)
array.sort()
for i in range(n):
    print(array[i])
