def find_digit(n, i):
    return (abs(n)//10**(i-1))%10 if i > 0 else -1
