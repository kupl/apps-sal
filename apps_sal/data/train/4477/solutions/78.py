def reverse_number(n):
    if n>0: return int(str(abs(n))[::-1])
    else: return int(str(abs(n))[::-1])*-1

