import re

def check_valid_tr_number(n):
    lst = list(map(int,str(n) if isinstance(n,int) else '0'))
    return (isinstance(n,int)
            and len(lst)==11 
            and sum(lst[:10]) % 10 == lst[-1]
            and (sum(lst[0:9:2])*7 - sum(lst[1:8:2])) % 10 == lst[-2])
