def super_size(n):
    ll = list()
    while n != 0:
        ll.append(n % 10)
        n //= 10
    ll = sorted(ll, reverse = True)
    res = 0
    
    for digit in ll:
        res = res * 10 + digit

    return res
