for _ in range(int(input())):
    sum_son = 0
    (n, k) = map(int, input().split())
    w = [int(item) for item in input().split()]
    w.sort()
    k = min(k, n - k)
    for i in range(k):
        sum_son = sum_son + w[i]
    total_sum = sum(w)
    chef_sum = total_sum - sum_son
    print(abs(chef_sum - sum_son))
