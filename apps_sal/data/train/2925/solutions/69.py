def multiply(n):
    lenght_of_n = len([i for i in str(n) if i.isdigit()])
    return n * 5 ** lenght_of_n
