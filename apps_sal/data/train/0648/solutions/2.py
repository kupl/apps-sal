(n, q) = list(map(int, input().split()))
hill = list(map(int, input().split()))


def get_answer_type_1(i, k):
    for ind in range(k):
        curr_elem = hill[i]
        for ind_sub in range(i, i + 101):
            try:
                this_elem = hill[ind_sub]
            except:
                break
            if this_elem > curr_elem:
                i = ind_sub
                break
    return i + 1


def get_answer_type_2(l, r, x):
    for ind in range(l, r + 1):
        hill[ind] += x


for i in range(q):
    query = input().split()
    if query[0] == '1':
        (i, k) = list(map(int, query[1:]))
        i -= 1
        print(get_answer_type_1(i, k))
    else:
        (l, r, x) = list(map(int, query[1:]))
        l -= 1
        r -= 1
        get_answer_type_2(l, r, x)
