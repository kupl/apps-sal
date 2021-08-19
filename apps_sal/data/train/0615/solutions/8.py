for case in range(int(input())):
    (n, q) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    dic = {0: 0}
    for i in range(1, n + 1):
        dic[i] = dic[i - 1] + arr[i - 1]
    for que in range(q):
        (xi, yi) = list(map(int, input().split()))
        print(dic[yi] - dic[xi - 1])
