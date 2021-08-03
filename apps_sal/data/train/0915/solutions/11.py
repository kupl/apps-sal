t = int(input())
while t != 0:
    dict = {}
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        if arr[i] in dict:
            dict[arr[i]] += 1
        else:
            dict[arr[i]] = 1
    print(len(dict))
    t -= 1
