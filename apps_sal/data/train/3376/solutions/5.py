def square_free_part(n):
    import math
    lst = []
    squares = []
    x = []
    if isinstance(n, int):
        if n > 1:
            for i in range(2, n // 2 + 1):
                if n % i == 0:
                    lst.append(i)
            lst.append(n)
            lst.reverse()
            for elem in lst:
                if math.sqrt(elem).is_integer():
                    squares.append(elem)
            for i in lst:
                for j in squares:
                    if i % j == 0:
                        break
                else:
                    x.append(i)
            if len(x) > 0:
                return x[0]
            else:
                return lst[0]
        elif n is 1:
            return 1
        else:
            return None
    else:
        return None
