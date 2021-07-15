from math import floor

def gap(g, m, n):
    for number in range(m, n+1):
        is_prime = True
        for divisor in range(2, floor(number**0.5)+1):
            if number % divisor == 0:
                is_prime = False
                break
                
        if is_prime:
            if 'prev_prime' not in locals():
                prev_prime = number
            else:
                if number - prev_prime == g:
                    return [prev_prime, number]
                else:
                    prev_prime = number

