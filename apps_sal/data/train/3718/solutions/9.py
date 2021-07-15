def divisors(n):
    divs = [] ## start empty list to store divisors
    for i in range(1,n + 1): ## loop through all numbers 1 to n 
        if n % i == 0: ## test if divisor
            divs.append(i) ##appends divisor
    return len(divs) ##return length of divisors


