def power_of_two(n):
    return True if n != 0 and 2 ** round(__import__('math').log(n, 2)) == n else False
