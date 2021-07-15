def last_man_standing(n):
    dir, lst = -1, range(2,n+1,2)
    while len(lst) != 1:
        lst = lst[len(lst)%2 or dir == 1 ::2]
        dir = -dir
    return lst[0]
