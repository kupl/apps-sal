def reverse_number(n):
    si =len(str(n))
    i = si 
    s = ''
    if n >= 0:
         while i > 0:
             s += str(n %10)
             n = n //10
             i -= 1
         return int(s)
    else:
        n = -1 * n
        while i > 1:
            s += str(n % 10)
            n = n // 10
            i -=1
        return -1 * int(s)

