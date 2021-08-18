try:
    n = int(input())

    list_n = list(range(1, n + 1))
    list_n_flag = []

    fix_arr = list(map(int, input().split()))

    k = 1
    res_list = []
    fin_list = []
    list_n_flag = list_n[k:] + list_n[:k]
    res_list = [list_n[i] + fix_arr[i] for i in range(len(fix_arr))]
    maxx = max(res_list)
    fin_list.append(maxx)
    while list_n != list_n_flag:

        res_list = [list_n_flag[i] + fix_arr[i] for i in range(len(fix_arr))]
        maxx = max(res_list)
        fin_list.append(maxx)
        list_n_flag = list_n_flag[k:] + list_n_flag[:k]

    print(*fin_list, sep=" ")
except:
    pass
