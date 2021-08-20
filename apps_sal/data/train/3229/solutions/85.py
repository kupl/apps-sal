def am_i_wilson(n):
    if n == 5 or n == 13 or n == 563:
        return True
    else:
        return False
    '\n    if n <= 2:\n        return False\n    fact=math.factorial(n-1)\n    if (fact+1)%n==0:\n        x = (fact+1)%(n**2)\n        if x==0:\n            return True\n        else:\n            return False\n    else:\n        return False\n    '
