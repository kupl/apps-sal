# cook your dish here
try:
    for i in range(int(input())):
        val = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        print(arr[0] + arr[1])
except:
    pass
