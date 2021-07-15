def balanced_num(number):
    digits = [int(digit) for digit in str(number)]
    n = len(digits)
    
    middle = [n // 2, n // 2 + 1] if n % 2 == 1 else [n // 2 - 1, n // 2 + 1]
    
    left = digits[:middle[0]]
    right = digits[middle[1]:]
    
    return "Balanced" if sum(left) == sum(right) else "Not Balanced"
