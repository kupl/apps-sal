def tv_remote(word):
    arr = ['abcde123', 'fghij456', 'klmno789', 'pqrst.@0', 'uvwxyz_/']
    res = 0
    start_i = 0
    start_j = 0
    for x in word:
        fin_i = 0
        for y in arr:
            if x in y:
                fin_i = arr.index(y)
                break

        res += abs(fin_i - start_i) + abs(arr[fin_i].index(x) - start_j) + 1
        start_i = fin_i
        start_j = arr[fin_i].index(x)
    return res
