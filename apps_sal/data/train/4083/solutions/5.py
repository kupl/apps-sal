def performant_smallest(arr, n):
    c = [0] * 51
    o = [0] * n
    # Count each number 1-50 in arr
    for i in arr:
        c[i] += 1
    # find least max number
    j, st = 0, (len(arr) - n)  # count of max numbers in arr
    for m in range(50, -1, -1):
        j += c[m]
        if j >= st:
            c[m] = j - st
            break  # m contains least max number
    j = 0
    # put elements from arr upto n, less than m upto c counts
    for i in arr:
        if i <= m and c[i] > 0:
            o[j] = i
            j += 1
            c[i] -= 1
        if j == n:  # out has all n elements for out
            break
    return o
