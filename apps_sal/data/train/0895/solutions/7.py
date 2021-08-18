n = int(input())
array = list(map(int, input().split()))
array2 = array.copy()
if n == 1:
    print(array)
elif n == 2:
    print(min(array[0], array[1]))
else:
    array[1] += array[0]
    for i in range(2, n):
        array[i] += min(array[i - 1], array[i - 2])
    minimo = min(array[-1], array[-2])
    array2[2] += array2[1]
    for i in range(3, n):
        array2[i] += min(array2[i - 1], array2[i - 2])
    print(min(minimo, array2[-1]))
