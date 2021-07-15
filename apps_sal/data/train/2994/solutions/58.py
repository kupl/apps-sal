def find_digit(num,n):
    return int(str(abs(num)).zfill(n+1)[-n]) if n>0 else -1
