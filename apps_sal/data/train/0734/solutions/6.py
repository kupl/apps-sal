for z in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dict_count = {}
    for num in a:
        if num in dict_count:
            dict_count[num] += 1
        else:
            dict_count[num] = 1
    possible = 1
    for key in dict_count:
        if dict_count[key] > n // 2:
            possible = 0
            break
    if possible:
        print('Yes')
        a_index = [(a[i], i) for i in range(n)]
        a_index.sort()
        cap_dict = {i: -1 for i in range(n)}
        h = n // 2
        for i in range(n):
            cap_dict[a_index[i][1]] = a_index[(i + h) % n][0]
        caps = [str(cap_dict[i]) for i in range(n)]
        print(' '.join(caps))
    else:
        print('No')
