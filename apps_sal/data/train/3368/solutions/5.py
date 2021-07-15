def is_prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return n > 1

def rotate(l, n):
    return l[-n:] + l[:-n]

def circular_prime(number):
    
    number_list = [int(x) for x in str(number)]
    if is_prime(number):
        check_list = [True]
        for index in range(1,len(number_list)):
            number_rotated = rotate(number_list,index)
            number_join = int(''.join(map(str, number_rotated)))
            if is_prime(number_join):
                check_list.append(True)
        if (len(check_list) == len(number_list)): return True
        else: return False
    else: return False
    
    

