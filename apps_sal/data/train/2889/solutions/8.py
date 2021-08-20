def count_ways(n, k):
    list_ = []
    for i in range(k):
        list_.append(2 ** i)
    print(list_)
    for i in range(n - k):
        list_.append(sum(list_[-k:]))
    print(list_)
    return list_[n - 1]
