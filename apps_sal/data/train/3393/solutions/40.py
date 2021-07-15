def map_sum_of_squqres(n):
    if n == 1:
        return [1,1]
    sum = 1 + n ** 2
    for i in range(2, int(n ** 0.5) + 1):
         if n % i == 0:
             sum += i ** 2
             if i != n / i:
                  sum += (n/i) ** 2
    return [n, sum]
    
def is_square(n):
    return int(n ** 0.5) ** 2 == n

def list_squared(m, n):
    return [i for i in map(map_sum_of_squqres, range(m,n+1)) if is_square(i[1])]
