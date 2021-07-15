def n_div(n):
    result = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            result += 1 + (i * i < n)
    return result
        

def find_min_num(num_div):
    for i in range(num_div, 1000000):
        if n_div(i) == num_div:
            return i
