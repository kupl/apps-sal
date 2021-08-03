def fact(n):

    res = 1

    for i in range(2, n + 1):
        res = res * i

    return res


def nCr(n, r):

    return (fact(n) / (fact(r)
                       * fact(n - r)))


for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    last_index_of_k = arr[k - 1]
    count = 0
    for i in range(n):
        if(arr[i] == last_index_of_k):
            count += 1
    num = 0
    for i in range(k):
        if(arr[i] == last_index_of_k):
            num += 1
    print(int(nCr(count, num)))
