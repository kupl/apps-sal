def factorsRange(n, m):
    i, dict = 2, {}
    for num in range(n, m + 1):
        while i < num:
            if num % i == 0 and num != i:
                dict.setdefault(num, []).append(i)
            i += 1
        i = 2
        if num not in dict:
            dict[num] = ['None']

    return dict
