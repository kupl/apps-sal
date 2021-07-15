def round_to_next5(n):
    # Your code here
    return 5 - n % 5 + n if n%5!=0  else n
