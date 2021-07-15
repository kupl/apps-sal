invalid=set()
def number_increasing(n):
    if n in invalid or n%5==0:return False
    while n>1:
        if n%3==0 and number_increasing(n//3):return True
        n -= 5
    if(n==1): return True
    invalid.add(n)
    return False
