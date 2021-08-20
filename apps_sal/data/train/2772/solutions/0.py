def mystery_solved(n):
    """
Recreated mystery function from bytecode using the dis module.
   How to print the bytecode: import dis
                              print(dis.dis(mystery)) 
    Apparently,                
    the function is a wrong implementation of the 5n+1 problem ->  
    https://math.stackexchange.com/questions/14569/the-5n1-problem
    http://www.sciencedirect.com/science/article/pii/S0304414905001602
    """
    c = 0
    while n != 1 and n != 13 and (n < 1000000):
        c = c + 1
        if n == 17:
            return -1
        if n & 1:
            n = n + n + n + n + n + 1
            continue
        n = n >> 1
    return c


def wrap_mystery(n):
    return mystery_solved(n)
