def strong_num(n):
    return 'STRONG!!!!' if sum(__import__('math').factorial(int(i)) for i in str(n)) == n else 'Not Strong !!'
