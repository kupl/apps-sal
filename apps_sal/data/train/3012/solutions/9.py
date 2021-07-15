def shared_bits(a, b):
    count = 0
    lst_a = list("{0:b}".format(a))
    lst_b = list("{0:b}".format(b))
    lst_a.reverse()
    lst_b.reverse()
    n_a = len(lst_a)
    n_b = len(lst_b)
    if(n_a == 0 or n_b == 0):
        return False
    else:
        if(n_a <= n_b):
            for i in range(n_a):
                if(lst_a[i] == lst_b[i] and lst_a[i] == "1"):
                    count += 1
                    if(count == 2):
                        return True
            return False
        else:
            for i in range(n_b):
                if(lst_a[i] == lst_b[i] and lst_b[i] == "1"):
                    count += 1
                    if(count == 2):
                        return True
            return False
