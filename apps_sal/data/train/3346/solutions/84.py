def gap(g, m, n):

    def prime(x):
        (i, answer) = (2, True)
        while i <= x ** 0.5:
            if x % i == 0:
                answer = False
                return answer
            i += 1
        return answer
    for i in range(m, n + 1):
        if prime(i):
            if prime(i + g):
                check = True
                for j in range(i + 2, i + g, 2):
                    if prime(j):
                        check = False
                        break
                if check:
                    return [i, i + g]
    return None
