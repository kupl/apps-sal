# cook your dish here
try:
    def inv(arr):
        arr1 = [0] * (len(arr))
        for i in range(len(arr)):
            arr1[arr[i] - 1] = i + 1
        return arr1

    t = int(input())
    while (t != 0):
        arr = list(map(int, input().split(' ')))
        arr1 = inv(arr)
        if (arr == arr1):
            print("ambiguous")
        else:
            print("not ambiguous")
        t = int(input())
except:
    pass
