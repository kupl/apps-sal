def square_it(digits):
    digits = str(digits)
    l = int(len(digits) ** 0.5)
    if l ** 2 == len(digits):
        return "\n".join(digits[i * l:i * l + l] for i in range(l))
    else:
        return "Not a perfect square!"
