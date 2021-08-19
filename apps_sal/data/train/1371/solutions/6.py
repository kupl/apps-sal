for t in range(int(input())):
    ip = list(map(int, input().split()))
    k = ip[1]
    array = list(map(int, input().split()))
    wolv = 0
    for i in range(ip[0]):
        array[i] += k
        if array[i] % 7 == 0:
            wolv += 1
    print(wolv)
