def automorphic(n):
    total = n * n
    total_lst = [i for i in str(total)]
    check_lst = [i for i in str(n)]
    back = len(check_lst)
    if check_lst == total_lst[-back:]:
        return 'Automorphic'
    else:
        return 'Not!!'
