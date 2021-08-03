def check(arr):
    c = 0
    for i in range(len(arr)):
        if i == len(arr) - 1:
            if arr[i] != arr[0]:
                c += 1
        elif arr[i] == '0' and arr[i + 1] == '1':
            c += 1
        elif arr[i] == '1' and arr[i + 1] == '0':
            c += 1
        if c > 2:
            return 'non-uniform'
    return 'uniform'


for __ in range(int(input())):
    arr = input()
    k = check(arr)
    print(k)
