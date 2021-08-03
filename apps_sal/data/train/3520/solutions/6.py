def step(g, m, n):
    def is_prime(n):
        if n == 2:
            return True
        elif n < 2 or n % 2 == 0:
            return False
        else:
            import math
            root = math.floor(math.sqrt(n))
            trial_factor = 3
            while trial_factor <= root:
                if n % trial_factor == 0:
                    return False
                trial_factor += 2
            return True
    dic = {}
    current_prime = None
    for i in range(m, n + 1):
        if is_prime(i):
            current_prime = i
            if current_prime - g in dic:
                return [current_prime - g, current_prime]
            else:
                dic[current_prime] = True

    return None

    # your code
