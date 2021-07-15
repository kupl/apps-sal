def getDivs(n):
    return {1} | {y for x in range(2,int(n**.5)+1) for y in [n//x, x] if not n%x}

def amicable_numbers(n1,n2):
    return sum(getDivs(n1)) == n2 and sum(getDivs(n2)) == n1
