def extra_perfect(n):
    return list(filter(lambda i: bin(i)[2] == '1' and bin(i)[-1] =='1', range(n+1)))
