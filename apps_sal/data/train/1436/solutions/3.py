# cook your dish here
def palin(arr):
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - 1 - i]:
            return -1
    return 1


t = int(input())
for _ in range(t):
    arr = input()
    if palin(arr) == 1:
        print(1)
    else:
        print(2)
