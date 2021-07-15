def powers_of_two(n):
    numbers=[]
    i = 0
    for i in range(0, n+1):
       numbers.append(2**i)
       if i == n:
            return(numbers)
