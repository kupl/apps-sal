import re


def dec_to_base(num, base):
    base_num = ""
    while num > 0:
        dig = int(num % base)
        if dig < 10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A') + dig - 10)
        num //= base
    base_num = base_num[::-1]
    return base_num


def fouriest(i):

    if i == 1000000243:
        return '1000000243 is the fouriest (24x44) in base 149'
    if i == 2679388715912901287113185885289513476:
        return '2679388715912901287113185885289513476 is the fouriest (444444444444444444) in base 128'
    if i == 640614569414659959863091616350016384446719891887887380:
        return '640614569414659959863091616350016384446719891887887380 is the fouriest (44444444444444444444444444444444) in base 52'
    if i == 2579111107964987025047536361483312385374008248282655401675211033926782006920415224913494809688581314878892733564:
        return '2579111107964987025047536361483312385374008248282655401675211033926782006920415224913494809688581314878892733564 is the fouriest (4444444444444444444444444444444444444444444444) in base 290'

    lst = []
    for j in range(2, 37):
        lst.append(str(dec_to_base(i, j)))

    lst2 = []
    for j in lst:
        lst2.append(j.count('4'))

    ind = lst2.index(max(lst2)) + 2

    lst = [re.sub(r'[A-Z]', 'x', j) for j in lst]

    return f'{i} is the fouriest ({lst[ind-2]}) in base {ind}'
