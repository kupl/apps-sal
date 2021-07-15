def amicable_numbers(n1,n2):
    s1 = sum([x for x in range(1,n1) if n1%x==0])
    s2 = sum([x for x in range(1,n2) if n2%x==0])
    return s1 == n2 and s2 == n1
