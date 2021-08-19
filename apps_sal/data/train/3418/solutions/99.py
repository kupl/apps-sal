def reverse_list(l):
    l.reverse()
    return l


l = [1, 2, 3, 4]
print('reverse_list(' + str(l) + ') == ' + str(reverse_list(l)))
l = [3, 1, 5, 4]
print('reverse_list(' + str(l) + ') == ' + str(reverse_list(l)))
