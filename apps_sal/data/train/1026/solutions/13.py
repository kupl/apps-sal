# cook your dish here
try:
    t = int(input())
    for jdnkjdew in range(t):
        arr = list(map(int, input().split()))
        arr.sort()
        a = arr[0] * (arr[1] - 1) * (arr[2] - 2)
        a %= 1000000007
        print(a)
except:
    pass
