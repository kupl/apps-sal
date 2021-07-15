def get_issuer(number):
    lst = list(str(number))
    n_len = len(lst)
    if (lst[0:2] == ['3', '4'] or lst[0:2] == ['3', '7']) and n_len == 15:
        return 'AMEX'
    elif lst[0:4] == ['6', '0', '1', '1'] and n_len == 16:
        return 'Discover'
    elif (lst[0] == '5' and lst[1] in ('1', '2', '3', '4', '5')) and n_len == 16:
        return 'Mastercard'
    elif lst[0] == '4' and (n_len == 13 or n_len == 16):
        return 'VISA'
    else:
        return 'Unknown'
