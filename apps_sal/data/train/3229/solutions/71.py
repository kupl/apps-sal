def am_i_wilson(n):
    if n in [5, 13, 563]:
        return True
    else:
        return False


'\ndef is_prime(n):\n    if n % 2 == 0 and n > 2: \n        return False\n    for i in range(3, int(n**0.5) + 1, 2):\n        if n % i == 0:\n            return False\n    return True  \n\ndef fac(n):\n    count = 1\n    for each in range(1, n + 1):\n        print(count)\n        count *= each\n    return count\n\ndef am_i_wilson(n):\n    print(n)\n    if n in (0,1):\n        return False\n    if is_prime(n):\n        tmp = (fac(n-1)+1)/(n**2)\n        if tmp == int(tmp):\n            return True\n    else:\n        return False \n'
